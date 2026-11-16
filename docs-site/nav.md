# Site nav

Read by mkdocs-literate-nav. Paths are relative to the repo root. Every markdown file outside the excluded directories needs a place here. prod-architect's sections, Architecture, Processes and Technical details, go after the Glossary; each writer adds its lines with its first page, since a glob matching nothing fails the strict build.

- [Home](README.md)
- [Glossary](GLOSSARY.md)
- Architecture
    - [Overview](docs/architecture/overview.md)
    - [Standards](docs/architecture/standards.md)
- Processes
    - [Deploying a component](docs/processes/deploy-a-component.md)
    - [Changing a standard](docs/processes/change-a-standard.md)
- [Resources catalog](catalog.md)
- Infrastructure (from src)
    - imported/infra/*.md
    - imported/infra/*/
- Issue tracker
    - [Backlog](.scratch/backlog.md)
    - .scratch/*/
