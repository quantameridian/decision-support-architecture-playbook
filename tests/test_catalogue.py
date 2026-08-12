"""Regression tests for catalogue traceability failures."""

from __future__ import annotations

import copy
import unittest

from scripts.validate_playbook_assets import load_catalogue, validate_catalogue


class CatalogueValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalogue = load_catalogue()

    def test_canonical_catalogue_is_valid(self) -> None:
        errors, _ = validate_catalogue(self.catalogue)
        self.assertEqual([], errors)

    def test_unknown_interface_component_is_rejected(self) -> None:
        changed = copy.deepcopy(self.catalogue)
        changed["interfaces"][0]["to"] = "CMP-99"
        errors, _ = validate_catalogue(changed)
        self.assertTrue(any("unknown to component CMP-99" in error for error in errors))

    def test_requirement_without_control_is_rejected(self) -> None:
        changed = copy.deepcopy(self.catalogue)
        for control in changed["controls"]:
            control["requirements"] = [
                requirement
                for requirement in control["requirements"]
                if requirement != "BR-03"
            ]
        errors, _ = validate_catalogue(changed)
        self.assertTrue(any("BR-03" in error for error in errors))

    def test_unknown_risk_control_is_rejected(self) -> None:
        changed = copy.deepcopy(self.catalogue)
        changed["risks"][0]["controls"] = ["CTL-99"]
        errors, _ = validate_catalogue(changed)
        self.assertTrue(any("unknown control CTL-99" in error for error in errors))

    def test_undefined_accountable_owner_is_rejected(self) -> None:
        changed = copy.deepcopy(self.catalogue)
        changed["requirements"][0]["owner"] = "Undefined Owner"
        errors, _ = validate_catalogue(changed)
        self.assertTrue(any("undefined owner Undefined Owner" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
