# The production playbook: the perimeter

Settled with the user in seat `prod-playbook`'s pane, 15 Nov 2026, by `grill-with-docs` (PP-Qn). Current decisions only; git holds their history.

The task (the user, 15 Nov ~21:14): one agent centralises and coordinates the creation and maintenance of a production maintenance playbook capturing the architecture, process and technical details, containing the resources catalog, in its own git repo, later with a Material for MkDocs web interface.

Production's shared rules (components, `component=` labels, names, addresses, deploys through WireGuard, host state directories) are in src's `infra/CONSTANTS.md`, section "Production" (integration a3d7c03); this repo follows them and does not restate them.

## Decided

- PP-Q1, the user, "the same as src's / freebsd-oci-containers' site" (22:33): the cut-off sentence meant the web interface is the same as those sites'.
- PP-Q2, "yes" (22:33): the deliverable is one playbook, and the cloud resources it uses, if any, appear in the catalog with deletion protection on. (The PDF part: PP-Q10.)
- PP-Q3, "yes" (22:33): production only, the `agentic-workflows` project (Phase 1a, 1b, 1c, later Phase 2); not cloud-sandbox, live-test, dev or the sandbox tooling. prod-architect writes the architecture, technical and processes sections (PA-Q17, the user, "yes", 21:58, relayed by the lead); prod-playbook writes the home page, the catalog page and the imported infra pages, and owns the repo, the build and the merges.
- PP-Q4, "yes" (22:33): this repo, `prod-playbook`, at `/agents/sessions/freebsd/sandbox/prod-playbook`, branch `main`.
- PP-Q5, "yes" (22:33): no remote; publishing to GitHub is asked as its own question once there is something to read.
- PP-Q6, "yes" (22:33): the playbook names where each secret lives and never holds one; a gitleaks pre-commit hook guards the repo.
- PP-Q7, "yes" (22:33): the build imports the infra READMEs and `CONSTANTS.md` from src at a named integration commit, read at build time, never committed here; each imported page shows its commit; the commit is a setting of this repo, moved forward by prod-playbook.
- PP-Q8, the user, "ask the prod-architect" (22:33): whether "prod-playbook owns the catalog" (PA-Q17) means the catalog page only or `infra/net/catalog` too goes to prod-architect through the lead. Open.
- PP-Q9, the user, "c, but can be served locally via `uv run mkdocs serve -f`" (22:33): no server of the playbook's own. Its reading is PP-Q15.
- PP-Q10, the user, "move PDF to phase 2" (22:33): no PDF in this iteration. Its reading is PP-Q16.
- PP-Q11, "yes" (22:33): `main` plus `feat/<topic>` branches in each writer's own worktree; only prod-playbook merges, `--no-ff`, after a `--strict` build passes on the branch, flagging to the lead a file both branches changed; the lead relays phase merges and deploys to whichever of the two owns the part affected.
- PP-Q12, "yes" (22:33): the rw token `agentic-workflows-prod-rw.token` while it exists, else the user makes one for the window and deletes it after.
- PP-Q13, the user, "yes, but name should be Production playbook" (22:33): src's MkDocs setup (`pyproject.toml` with `mkdocs-material==9.7.7` and `mkdocs-literate-nav` under `uv`, `docs-site/` with `mkdocs.yml` and `nav.md`, the repo as the site, the same theme and extensions, `--strict`, commitizen and pre-commit with gitleaks); `site_name: Production playbook`.
- PP-Q14, "yes" (22:33): before merging prod-architect's branches, prod-playbook checks only the `--strict` build, the render and gitleaks; a visual change is shown to the user as a render before it is committed.
