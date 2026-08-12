# Contributing

Changes are welcome when they improve correctness, traceability or practical use.

## Before A Pull Request

1. Keep the Operations Review Service scenario synthetic.
2. Do not add real organisation names, system inventories, routes, credentials, incidents or meeting records.
3. Update `catalogue/architecture.yaml` first when changing a requirement, component, interface, control, risk or decision.
4. Add a new ADR when an accepted choice changes. Do not rewrite an accepted record.
5. Update the affected diagram and operating document.
6. Run `make qa` and commit the regenerated validation evidence.

## Review Standard

A change should answer why it is needed, which requirement or risk it affects, who owns it and how acceptance would be evidenced. Extra governance language without a clearer decision, control or operating outcome is not useful.
