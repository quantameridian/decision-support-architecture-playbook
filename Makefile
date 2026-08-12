.PHONY: install test validate diagrams audit report qa

PYTHON ?= python3

install:
	$(PYTHON) -m pip install -r requirements-dev.txt
	npm ci

test:
	$(PYTHON) -m unittest discover -s tests -v

validate:
	$(PYTHON) scripts/validate_playbook_assets.py

diagrams:
	npm run validate:diagrams

audit:
	npm audit --audit-level=moderate
	$(PYTHON) -m pip_audit -r requirements.txt

report:
	$(PYTHON) scripts/validate_playbook_assets.py --write-report

qa: test validate diagrams audit report
