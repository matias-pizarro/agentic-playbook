# Glossary

**Production**: the Hetzner Cloud project `agentic-workflows`, and only it.
_Avoid_: prod environment, live

**Component**: a part of the platform that owns its resources and has one builder seat. The list is [COMPONENTS.md](imported/infra/COMPONENTS.md). Production's components are `net`, `sylve`, `vikunja`, `zulip` and `playbook`; besides them are `certificates-acme` and `sandbox-host`, each in a project of its own, and `sandbox`, the sandbox tool. A resource belongs to a component, not to the seat that built it.
_Avoid_: seat (a seat is an agent; it may be assigned a component)

**Playbook**: this repo's documentation of how production is built and maintained: its architecture, processes and technical details, and the catalog.
_Avoid_: runbook, wiki

**Catalog**: the list of every resource in production, generated from the project itself.
_Avoid_: inventory, resource list
