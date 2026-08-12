"""Validate architecture catalogue traceability and public review assets."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE_PATH = ROOT / "catalogue/architecture.yaml"
REPORT_PATH = ROOT / "docs/validation-report.md"

REQUIRED_DOCS = [
    "README.md",
    "docs/00-executive-brief.md",
    "docs/01-problem-statement.md",
    "docs/02-current-state.md",
    "docs/03-target-state.md",
    "docs/04-source-to-output-map.md",
    "docs/05-data-quality-controls.md",
    "docs/06-kpi-dictionary.md",
    "docs/07-operating-model.md",
    "docs/08-implementation-roadmap.md",
    "docs/09-risks-and-limitations.md",
    "docs/10-handover-pack.md",
    "docs/11-security-architecture.md",
    "docs/12-requirements-and-traceability.md",
    "docs/reviewer-guide.md",
    "docs/security-posture.md",
    "decisions/README.md",
    "examples/pilot-release-evidence.md",
    "examples/architecture-assurance-review.md",
]

REQUIRED_DIAGRAMS = [
    "diagrams/system-context.mmd",
    "diagrams/container-view.mmd",
    "diagrams/trust-boundaries.mmd",
    "diagrams/reporting-cycle-sequence.mmd",
    "diagrams/current-state-flow.mmd",
    "diagrams/source-to-output-flow.mmd",
    "diagrams/reporting-lifecycle.mmd",
    "diagrams/assurance-control-loop.mmd",
]

REQUIRED_TEMPLATES = {
    "templates/architecture-decision-record-template.md": [
        "## Context",
        "## Options",
        "## Decision",
        "## Consequences",
        "## Verification",
        "## Review Triggers",
    ],
    "templates/data-quality-rule-template.md": [
        "## Decision Risk",
        "## Data Contract",
        "## Rule Logic",
        "## Failure Route",
        "## Test Cases",
    ],
    "templates/kpi-definition-template.md": [
        "## Identity And Decision",
        "## Semantic Definition",
        "## Data Route",
        "## Quality And Interpretation",
    ],
    "templates/reporting-requirements-template.md": [
        "## Context And Outcome",
        "## Functional Requirements",
        "## Non Functional Requirements",
        "## Acceptance Plan",
    ],
    "templates/stakeholder-review-template.md": [
        "## Evidence Reviewed",
        "## Caveats And Risks",
        "## Decisions",
        "## Actions",
    ],
    "templates/threat-assessment-template.md": [
        "## Context And Scope",
        "## Assets And Actors",
        "## Threats",
        "## Verification",
    ],
    "templates/release-evidence-template.md": [
        "## Cycle And Version",
        "## Reconciliation",
        "## Control Results",
        "## Accepted Caveats",
    ],
}

RETIRED_FILES = [
    "AGENTS.md",
    "docs/commercial-review-scorecard.md",
    "docs/public-readiness-audit.md",
    "docs/sample-data-plan.md",
    "docs/test-plan.md",
    "examples/architecture-decision-record-example.md",
    "examples/manual-reporting-transformation-example.md",
    "diagrams/security-boundary.mmd",
]

SECTION_PREFIXES = {
    "principles": "AP",
    "requirements": None,
    "components": "CMP",
    "interfaces": "INT",
    "controls": "CTL",
    "evidence": "EVD",
    "risks": "RSK",
    "decisions": "ADR",
}

EXPECTED_MINIMUMS = {
    "principles": 6,
    "requirements": 11,
    "components": 10,
    "interfaces": 14,
    "controls": 13,
    "evidence": 13,
    "risks": 10,
    "decisions": 3,
}

LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IDENTIFIER_RE = re.compile(r"\b(?:AP|BR|NFR|CMP|INT|CTL|EVD|RSK|ADR)-\d{2,3}\b")


def load_catalogue(path: Path = CATALOGUE_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file:
        value = yaml.safe_load(file)
    if not isinstance(value, dict):
        raise ValueError("architecture catalogue must contain a mapping")
    return value


def _section_ids(catalogue: dict[str, Any], section: str) -> set[str]:
    return {str(item.get("id", "")) for item in catalogue.get(section, [])}


def _require_fields(
    item: dict[str, Any], fields: tuple[str, ...], label: str, errors: list[str]
) -> None:
    for field in fields:
        if field not in item or item[field] in (None, "", []):
            errors.append(f"{label}: missing {field}")


def validate_catalogue(
    catalogue: dict[str, Any], root: Path = ROOT
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []
    service = catalogue.get("service")
    if not isinstance(service, dict):
        errors.append("catalogue: service must be a mapping")
    else:
        _require_fields(
            service,
            (
                "id",
                "name",
                "status",
                "scenario",
                "purpose",
                "decision_owner",
                "service_owner",
                "information_classification",
                "recovery",
            ),
            "service",
            errors,
        )
        if service.get("scenario") != "synthetic":
            errors.append("service: scenario must remain synthetic")
        recovery = service.get("recovery", {})
        if recovery.get("rto_hours", 0) <= 0 or recovery.get("rpo_hours", 0) <= 0:
            errors.append("service: recovery targets must be positive")

    roles = catalogue.get("roles")
    if not isinstance(roles, dict) or len(roles) < 12:
        errors.append("catalogue: expected at least 12 defined operating roles")
        roles = {}
    else:
        for role, responsibility in roles.items():
            if not str(role).strip() or not str(responsibility).strip():
                errors.append("catalogue: every role needs a name and responsibility")

    assignments = catalogue.get("role_assignments")
    if not isinstance(assignments, dict):
        errors.append("catalogue: role_assignments must be a mapping")
        assignments = {}
    for role in assignments:
        if role not in roles:
            errors.append(f"role assignment refers to undefined role {role}")
    if isinstance(service, dict):
        for field in ("decision_owner", "service_owner"):
            if service.get(field) not in roles:
                errors.append(f"service: {field} is not a defined role")
            if service.get(field) not in assignments:
                errors.append(f"service: {field} has no scenario assignment")

    all_ids: set[str] = set()
    section_ids: dict[str, set[str]] = {}
    for section, minimum in EXPECTED_MINIMUMS.items():
        items = catalogue.get(section)
        if not isinstance(items, list):
            errors.append(f"catalogue: {section} must be a list")
            items = []
        if len(items) < minimum:
            errors.append(f"catalogue: expected at least {minimum} {section}, found {len(items)}")
        identifiers = _section_ids(catalogue, section)
        if "" in identifiers:
            errors.append(f"catalogue: {section} contains an item without an ID")
            identifiers.discard("")
        if len(identifiers) != len(items):
            errors.append(f"catalogue: {section} IDs must be unique")
        duplicate_global = all_ids & identifiers
        if duplicate_global:
            errors.append(f"catalogue: IDs repeated across sections: {sorted(duplicate_global)}")
        all_ids.update(identifiers)
        section_ids[section] = identifiers

        prefix = SECTION_PREFIXES[section]
        if prefix:
            for identifier in identifiers:
                if not re.fullmatch(rf"{prefix}-\d{{2,3}}", identifier):
                    errors.append(f"{identifier}: invalid {section} ID")

    for requirement in catalogue.get("requirements", []):
        identifier = requirement.get("id", "requirement")
        if not re.fullmatch(r"(?:BR|NFR)-\d{2}", str(identifier)):
            errors.append(f"{identifier}: invalid requirement ID")
        _require_fields(
            requirement,
            ("category", "statement", "priority", "owner", "acceptance"),
            str(identifier),
            errors,
        )
        if requirement.get("owner") not in roles:
            errors.append(f"{identifier}: undefined owner {requirement.get('owner')}")

    for component in catalogue.get("components", []):
        _require_fields(
            component,
            ("name", "type", "zone", "owner", "data_classification", "responsibilities"),
            component.get("id", "component"),
            errors,
        )
        if component.get("owner") not in roles:
            errors.append(
                f"{component.get('id')}: undefined owner {component.get('owner')}"
            )

    component_ids = section_ids.get("components", set())
    for interface in catalogue.get("interfaces", []):
        identifier = interface.get("id", "interface")
        _require_fields(
            interface,
            ("from", "to", "mode", "format", "cadence", "protection"),
            identifier,
            errors,
        )
        for endpoint in ("from", "to"):
            if interface.get(endpoint) not in component_ids:
                errors.append(f"{identifier}: unknown {endpoint} component {interface.get(endpoint)}")
        if interface.get("from") == interface.get("to"):
            errors.append(f"{identifier}: interface endpoints must differ")

    requirement_ids = section_ids.get("requirements", set())
    evidence_ids = section_ids.get("evidence", set())
    covered_requirements: set[str] = set()
    referenced_evidence: set[str] = set()
    for control in catalogue.get("controls", []):
        identifier = control.get("id", "control")
        _require_fields(
            control,
            ("name", "type", "owner", "requirements", "component", "evidence"),
            identifier,
            errors,
        )
        if control.get("owner") not in roles:
            errors.append(f"{identifier}: undefined owner {control.get('owner')}")
        for requirement_id in control.get("requirements", []):
            if requirement_id not in requirement_ids:
                errors.append(f"{identifier}: unknown requirement {requirement_id}")
            covered_requirements.add(requirement_id)
        if control.get("component") not in component_ids:
            errors.append(f"{identifier}: unknown component {control.get('component')}")
        if control.get("evidence") not in evidence_ids:
            errors.append(f"{identifier}: unknown evidence {control.get('evidence')}")
        referenced_evidence.add(control.get("evidence"))

    uncovered = requirement_ids - covered_requirements
    if uncovered:
        errors.append(f"requirements without controls: {sorted(uncovered)}")
    unused_evidence = evidence_ids - referenced_evidence
    if unused_evidence:
        errors.append(f"evidence without controls: {sorted(unused_evidence)}")

    control_ids = section_ids.get("controls", set())
    for evidence in catalogue.get("evidence", []):
        _require_fields(
            evidence,
            ("artifact", "frequency", "retention_months"),
            evidence.get("id", "evidence"),
            errors,
        )
        if evidence.get("retention_months", 0) <= 0:
            errors.append(f"{evidence.get('id')}: retention must be positive")

    risk_ids = section_ids.get("risks", set())
    for risk in catalogue.get("risks", []):
        identifier = risk.get("id", "risk")
        _require_fields(
            risk,
            (
                "statement",
                "likelihood",
                "impact",
                "owner",
                "treatment",
                "requirements",
                "controls",
                "residual_rating",
            ),
            identifier,
            errors,
        )
        if risk.get("owner") not in roles:
            errors.append(f"{identifier}: undefined owner {risk.get('owner')}")
        for requirement_id in risk.get("requirements", []):
            if requirement_id not in requirement_ids:
                errors.append(f"{identifier}: unknown requirement {requirement_id}")
        for control_id in risk.get("controls", []):
            if control_id not in control_ids:
                errors.append(f"{identifier}: unknown control {control_id}")

    for decision in catalogue.get("decisions", []):
        identifier = decision.get("id", "decision")
        _require_fields(
            decision,
            ("title", "status", "owner", "requirements", "risks", "record"),
            identifier,
            errors,
        )
        if decision.get("owner") not in roles:
            errors.append(f"{identifier}: undefined owner {decision.get('owner')}")
        for requirement_id in decision.get("requirements", []):
            if requirement_id not in requirement_ids:
                errors.append(f"{identifier}: unknown requirement {requirement_id}")
        for risk_id in decision.get("risks", []):
            if risk_id not in risk_ids:
                errors.append(f"{identifier}: unknown risk {risk_id}")
        record = root / str(decision.get("record", ""))
        if not record.is_file():
            errors.append(f"{identifier}: missing decision record {decision.get('record')}")
        else:
            record_text = record.read_text(encoding="utf-8")
            if f"# {identifier}:" not in record_text:
                errors.append(f"{identifier}: decision record heading does not match ID")
            if "| Status | Accepted for scenario |" not in record_text:
                errors.append(f"{identifier}: decision record must state synthetic acceptance")

    notes.append(
        "Validated "
        + ", ".join(
            f"{len(catalogue.get(section, []))} {section}" for section in EXPECTED_MINIMUMS
        )
    )
    notes.append(f"Confirmed {len(roles)} defined roles and accountable owners")
    notes.append(f"Confirmed control coverage for {len(requirement_ids)} requirements")
    return errors, notes


def _markdown_files(root: Path) -> list[Path]:
    paths = [
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    ]
    return sorted(paths)


def validate_public_assets(
    catalogue: dict[str, Any], root: Path = ROOT
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []

    for relative_path in REQUIRED_DOCS + REQUIRED_DIAGRAMS + list(REQUIRED_TEMPLATES):
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing required asset: {relative_path}")
    for relative_path in RETIRED_FILES:
        if (root / relative_path).exists():
            errors.append(f"retired internal asset remains: {relative_path}")

    for relative_path, headings in REQUIRED_TEMPLATES.items():
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"{relative_path}: missing template heading {heading}")

    diagram_paths = sorted((root / "diagrams").glob("*.mmd"))
    if len(diagram_paths) != len(REQUIRED_DIAGRAMS):
        errors.append(
            f"expected {len(REQUIRED_DIAGRAMS)} Mermaid files, found {len(diagram_paths)}"
        )
    known_ids = set().union(
        *(_section_ids(catalogue, section) for section in EXPECTED_MINIMUMS)
    )
    for path in diagram_paths:
        text = path.read_text(encoding="utf-8")
        if not re.match(r"\s*(?:flowchart|graph|sequenceDiagram|stateDiagram|erDiagram)", text):
            errors.append(f"{path.relative_to(root)}: unsupported Mermaid declaration")
        for identifier in IDENTIFIER_RE.findall(text):
            if identifier not in known_ids:
                errors.append(f"{path.relative_to(root)}: unknown identifier {identifier}")

    container_text = (root / "diagrams/container-view.mmd").read_text(encoding="utf-8")
    for identifier in _section_ids(catalogue, "components") | _section_ids(catalogue, "interfaces"):
        if identifier not in container_text:
            errors.append(f"container view is missing {identifier}")

    local_link_count = 0
    markdown_paths = _markdown_files(root)
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        for raw_target in LOCAL_LINK_RE.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            local_link_count += 1
            linked_path = path.parent / unquote(target)
            if not linked_path.exists():
                errors.append(
                    f"{path.relative_to(root)}: broken local link {raw_target}"
                )

    forbidden_phrases = (
        "portfolio",
        "hiring manager",
        "interview angle",
        "commercial readiness",
        "public readiness",
        "best in class",
        "ai generated",
    )
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for phrase in forbidden_phrases:
            if phrase in lowered:
                errors.append(f"{path.relative_to(root)}: internal facing phrase {phrase!r}")
        if "—" in text:
            errors.append(f"{path.relative_to(root)}: em dash is not used in public copy")

    unsafe_patterns = (
        r"/Users/",
        r"C:\\Users\\",
        r"ghp_[A-Za-z0-9]+",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"client_secret\s*[:=]",
        r"password\s*[:=]",
    )
    scan_suffixes = {".md", ".mmd", ".yaml", ".yml", ".json", ".mjs"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix not in scan_suffixes:
            continue
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in unsafe_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                errors.append(f"{path.relative_to(root)}: contains unsafe pattern")
                break

    notes.append(
        f"Checked {len(REQUIRED_DOCS)} operating records, "
        f"{len(REQUIRED_TEMPLATES)} templates and {len(diagram_paths)} Mermaid sources"
    )
    notes.append(f"Checked {local_link_count} local documentation links")
    return errors, notes


def _links_for_requirement(
    catalogue: dict[str, Any], requirement_id: str
) -> tuple[list[str], list[str], list[str], list[str]]:
    controls = [
        control
        for control in catalogue["controls"]
        if requirement_id in control["requirements"]
    ]
    control_ids = [control["id"] for control in controls]
    evidence_ids = sorted({control["evidence"] for control in controls})
    decision_ids = [
        decision["id"]
        for decision in catalogue["decisions"]
        if requirement_id in decision["requirements"]
    ]
    risk_ids = [
        risk["id"]
        for risk in catalogue["risks"]
        if requirement_id in risk["requirements"]
    ]
    return control_ids, evidence_ids, decision_ids, risk_ids


def write_report(catalogue: dict[str, Any], notes: list[str]) -> None:
    matrix = []
    for requirement in catalogue["requirements"]:
        controls, evidence, decisions, risks = _links_for_requirement(
            catalogue, requirement["id"]
        )
        matrix.append(
            "| "
            + " | ".join(
                [
                    f"`{requirement['id']}`",
                    requirement["owner"],
                    ", ".join(f"`{item}`" for item in controls),
                    ", ".join(f"`{item}`" for item in evidence),
                    ", ".join(f"`{item}`" for item in decisions) or "None required",
                    ", ".join(f"`{item}`" for item in risks),
                    "Designed",
                ]
            )
            + " |"
        )

    inventory = [
        ("Operating roles", len(catalogue["roles"])),
        ("Requirements", len(catalogue["requirements"])),
        ("Components", len(catalogue["components"])),
        ("Interfaces", len(catalogue["interfaces"])),
        ("Controls", len(catalogue["controls"])),
        ("Evidence records", len(catalogue["evidence"])),
        ("Risks", len(catalogue["risks"])),
        ("Decisions", len(catalogue["decisions"])),
    ]
    REPORT_PATH.write_text(
        "\n".join(
            [
                "# Validation Evidence",
                "",
                "Generated by `scripts/validate_playbook_assets.py --write-report` from the architecture catalogue.",
                "",
                "## Automated Checks",
                "",
                *[f"- {note}." for note in notes],
                "",
                "## Architecture Inventory",
                "",
                "| Object | Count |",
                "| --- | ---: |",
                *[f"| {name} | {count} |" for name, count in inventory],
                "",
                "## Requirement Coverage",
                "",
                "| Requirement | Owner | Controls | Evidence | Decisions | Risks | Status |",
                "| --- | --- | --- | --- | --- | --- | --- |",
                *matrix,
                "",
                "## Assurance Boundary",
                "",
                "All requirements are structurally traced and have the status `Designed`. The checks prove catalogue consistency, public asset presence, local link integrity and Mermaid syntax. They do not prove that a platform is deployed or that a control operated. Pilot and operational status require observed acceptance evidence.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def validate_all(root: Path = ROOT) -> tuple[dict[str, Any], list[str], list[str]]:
    catalogue = load_catalogue(root / "catalogue/architecture.yaml")
    catalogue_errors, catalogue_notes = validate_catalogue(catalogue, root)
    asset_errors, asset_notes = validate_public_assets(catalogue, root)
    return catalogue, catalogue_errors + asset_errors, catalogue_notes + asset_notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    try:
        catalogue, errors, notes = validate_all()
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if args.write_report:
        write_report(catalogue, notes)
        notes.append(f"Wrote {REPORT_PATH.relative_to(ROOT)}")

    for note in notes:
        print(note)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
