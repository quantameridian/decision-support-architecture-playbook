.PHONY: test validate report qa

PYTHON ?= python3

test validate:
	$(PYTHON) scripts/validate_playbook_assets.py

report:
	$(PYTHON) scripts/validate_playbook_assets.py --write-report

qa: report
