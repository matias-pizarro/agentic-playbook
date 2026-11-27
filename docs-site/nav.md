# Site nav

Read by mkdocs-literate-nav. Paths are relative to the repo root. Every markdown file outside the excluded directories needs a place here. prod-architect's sections, Architecture, Processes and Technical details, go after the Glossary; each writer adds its lines with its first page, since a glob matching nothing fails the strict build.

- [Home](README.md)
- [Glossary](GLOSSARY.md)
- Architecture
    - [Overview](docs/architecture/overview.md)
    - [Standards](docs/architecture/standards.md)
    - [Request journeys](docs/architecture/request-journeys.md)
- Processes
    - [Deploying a component](docs/processes/deploy-a-component.md)
    - [Changing a standard](docs/processes/change-a-standard.md)
    - [Work items in Vikunja](docs/processes/work-items-in-vikunja.md)
    - [Setting up the ACME validation zone](docs/processes/acme-validation-zone.md)
- [Resources catalog](catalog.md)
- Infrastructure (from src)
    - imported/infra/*.md
    - imported/infra/*/
- Issue tracker
    - [Backlog](.scratch/backlog.md)
    - .scratch/*/
