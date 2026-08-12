# Diagram Index

The diagrams are source files that GitHub can render and reviewers can diff. Component and interface identifiers come from the [architecture catalogue](../catalogue/architecture.yaml).

| View | Question answered |
| --- | --- |
| [system context](system-context.mmd) | Who uses the service and which external systems does it depend on? |
| [container view](container-view.mmd) | Which logical components own each responsibility and interface? |
| [trust boundaries](trust-boundaries.mmd) | Where do data and identity cross security zones? |
| [reporting cycle sequence](reporting-cycle-sequence.mmd) | In what order are source, quality, approval and decision evidence created? |
| [current state](current-state-flow.mmd) | Where are the present manual dependencies? |
| [source to output](source-to-output-flow.mmd) | How does a record become a management output and action? |
| [reporting lifecycle](reporting-lifecycle.mmd) | How does review feed changes into the next cycle? |
| [assurance loop](assurance-control-loop.mmd) | How are quality exceptions corrected or escalated? |

`npm run validate:diagrams` sends every `.mmd` file through Mermaid syntax parsing. A diagram also needs human review: valid syntax does not prove correct boundaries, direction or ownership.
