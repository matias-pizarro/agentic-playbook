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
- PP-Q8, the user, "ask the prod-architect" (22:33); prod-architect's answer, relayed by the lead from src's `.scratch/prod-architect/perimeter.md` (a3d7c03): PA-Q17 gives prod-playbook the catalog's page and place in the playbook only; the generating script `infra/net/catalog` stays net's in src (PN-Q7, PN-Q22; PA-Q4: code and rules stay in src). The playbook's build runs it with the read-only token and includes the HTML it writes.
- PP-Q9, the user, "c, but can be served locally via `uv run mkdocs serve -f`" (22:33), read by PP-Q15, "yes" (22:50): the playbook is served on this machine with `uv run mkdocs serve -f docs-site/mkdocs.yml` and has no cloud resource now, so no catalog entry and nothing to protect; later it is served from a jail on the sylve server, which sylve's component adds, asked then.
- PP-Q10, the user, "move PDF to phase 2" (22:33), read by PP-Q16, "yes" (22:50): the PDF export comes with the infrastructure Phase 2; a backlog entry holds it.
- PP-Q17, "yes" (22:50): the repo is built now; only the catalog page waits, for net's Phase 1a merge and its resources in production.
- PP-Q18, "yes" (22:50): one ticket, implemented at tier `checklist`.
- PP-Q19, the user, "B, you are allowed to create that code this time" (15 Nov, between 22:50 and 23:11): `docs-site/hooks.py` turns an imported page's link to a src file the playbook lacks into plain text naming it in src at the imported commit; the strict build keeps failing on the playbook's own broken links.
- PP-Q20, "yes, a leftover" (with PP-Q19): the stray "PP-Q16" line meant nothing more.
- PP-Q21, the user, "A" (23:33): the infra section imports the prototypes' pages, titled as such, until the production phases merge; prod-playbook moves `src_commit` forward at each merge.
- PP-Q22, "yes" (23:33): the render (home and an imported page) is right; the site is committed to `main`.
- PP-Q23, the user, "B" (16 Nov, before 00:03): the catalog is shown inside the playbook's frame, a page `catalog.md` holding net's HTML in a full-width iframe, with a link to it on its own page.
- PP-Q24, "yes" (with PP-Q23): the catalog page and src at ec6c118 are committed.
- PP-Q26, the user, "yes" (18 Nov 07:59): the page of the team's slash commands and prompts lives in agentic_workflow's own `docs/commands.md`, written by its seat through the lead; the playbook stays production-only (PP-Q3) and does not import it.
- PP-Q25, the user, "yes" (16 Nov 14:41): the framed catalog page as committed (2166156) stays, full-width with no side navigation; it was committed first as a rehearsal assumption under the overnight rehearsal (guardrail 4).
- PP-Q11, "yes" (22:33): `main` plus `feat/<topic>` branches in each writer's own worktree; only prod-playbook merges, `--no-ff`, after a `--strict` build passes on the branch, flagging to the lead a file both branches changed; the lead relays phase merges and deploys to whichever of the two owns the part affected.
- PP-Q12, "yes" (22:33): the rw token `agentic-workflows-prod-rw.token` while it exists, else the user makes one for the window and deletes it after.
- PP-Q13, the user, "yes, but name should be Production playbook" (22:33): src's MkDocs setup (`pyproject.toml` with `mkdocs-material==9.7.7` and `mkdocs-literate-nav` under `uv`, `docs-site/` with `mkdocs.yml` and `nav.md`, the repo as the site, the same theme and extensions, `--strict`, commitizen and pre-commit with gitleaks); `site_name: Production playbook`.
- PP-Q14, "yes" (22:33): before merging prod-architect's branches, prod-playbook checks only the `--strict` build, the render and gitleaks; a visual change is shown to the user as a render before it is committed.

- PP-Q5 superseded (the user, CS-Q82, "Yes", lead pane 22 Nov 22:14; relayed by the lead 23 Nov 23:00): the playbook has a private remote, `git@github-agentic-playbook:matias-pizarro/agentic-playbook.git`; the standing push go covers `main` of that repo only, after a gitleaks pass. First push 23 Nov 23:09, at 4b56202.

The docs jail (the user, "Task an agent with create a docs jail in sylve", 20 Nov 2026 20:10; held by the lead 21 Nov 10:41); answers of 23 Nov 2026, prod-playbook pane, 23:08:

- PP-Q27, the user, "I don't think it makes sense to separate the 3 documenation streams. What does each focus on?" (23:08); then "Yes" (23:40): the docs jail serves one combined site, with Production, Sandboxes and Method sections: the playbook, src's docs and agentic_workflow's docs, each kept in its own repo with its writers and imported at a named commit at build time, built and served by prod-playbook. This replaces PP-Q3's production-only scope and PP-Q26's exclusion of agentic_workflow's pages.
- PP-Q34, "Yes" (23:40): the docs jail stays on hold until the docs overhaul's turn, its answers kept as recorded.
- PP-Q28, "Yes": served only to WireGuard peers, through Sylve's reverse proxy jail over TLS at a name such as `docs.dkl.cat`, with a DNS-01 certificate; nothing reachable from the internet.
- PP-Q29, "Yes": its readers are Sylve's peers, the user's laptop (10.131.0.2) and the deploy peer (10.131.0.3).
- PP-Q30, "Yes": a dedicated `docs` jail on sylve-server serving static files to the proxy only; the real free disk and a jail's real cost are read before the design rests on them.
- PP-Q31, the user, "src's and agentic_workflow's docs, are in scope (see PP-Q27)": the other items proposed out of scope (internet exposure, a forge, logins beyond WireGuard, search or analytics, content changes) were not named in the answer.

The term "remote sandbox" (the user, "it should be `remote sandboxes` instead of `jailed sandboxes`", lead pane 22 Nov 22:14):

- PP-Q32, "Yes" (23 Nov 23:08): "remote sandbox" names a jail sandbox running on a sandbox host rather than the user's own machine; "jail sandbox" stays the model's name; src's GLOSSARY.md gets the entry and Cloud sandbox drops it from its Avoid line.
- PP-Q33, "Yes" (23 Nov 23:08): tier `docs`; prod-playbook writes the glossary lines on its own src branch, merged on the lead's authorisation; sandbox-host renames the two lines in its `.scratch/sandbox-host/defaults.md`.
- PP-Q36, "Yes" (26 Nov 21:26): src's glossary gets a "Local sandbox" entry, a container on the user's own host, and its Sandbox entry names the three kinds, local, remote and cloud; written on src `docs/local-sandbox`, shown to the user before it merges.
- PP-Q35, "Yes" (23 Nov 23:40): the glossary change on src `docs/remote-sandbox` at 0f2a2ccc is right as written, to merge on the lead's authorisation.
