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
- PP-Q37, "yes" (26 Nov 21:28): the "Local sandbox" change on src `docs/local-sandbox` at 987b7358 is right as written, to merge on the lead's authorisation.
- PP-Q35, "Yes" (23 Nov 23:40): the glossary change on src `docs/remote-sandbox` at 0f2a2ccc is right as written, to merge on the lead's authorisation.
- From 27 Nov 2026 the seat is librarian, and its question IDs are LB-Qn.
- LB-Q2, "yes" (the user, librarian pane, 27 Nov 2026 21:19): `docs/processes/deploy-a-component.md` steps 2 and 8 read `wg-quick up prod-agt-deploy` and `wg-quick down prod-agt-deploy` (CS-Q97 (a), tier `docs`).
- LB-Q3, "(b) As (a), plus a sweep of the other 25 pages for the same kind of history" (the user, librarian pane, 27 Nov 2026 21:19), after "we don't need history and past phases. only the current state and any relevant future phase" (21:16) on the architecture overview. The overview's text drops past phases, build dates and how things were built, tier `docs`; the platform diagram's phase labels go in CS-Q98's `vg` render, and LB-Q1's commit waits for that render; every other page is swept for the same kind of history.
- LB-Q4, "Yes" (the user, librarian pane, 27 Nov 2026 21:29): the overview and its diagrams are rewritten to production's current state, from architect's facts of 27 Nov 21:20, with no future-phases section, since none is defined. Architect checks the facts, and the user sees the renders before the commit. LB-Q1 is withdrawn: settled by LB-Q3.
- LB-Q5, "Yes" (21:29): librarian fixes the playbook's own pages, keeping decision citations and verification records. Each owner gets a list, through the lead, of the history lines in its page imported from src. The issue tracker pages are left out. The same message: "The librarian does not write for them but keeps them honest and up to date"; coach is asked to reflect on how librarian stays accountable for the docs' freshness as other seats change the ground truth.
- LB-Q7, "LB-Q6,7 yes" (the user, librarian pane, 27 Nov 2026 21:37): the overview, `platform` and `deploy-flow` renders are approved, after architect's fact check (clear once the proxy-to-Vikunja edge read `http :3456`). The `phase-2` diagram is removed.
- LB-Q6, the same message: "Renewing Vikunja's certificate" is deleted; "Work items in Vikunja" is rewritten to its current state; "Setting up the ACME validation zone" is trimmed to the steps for recreating the zone.
- LB-Q8, "yes" (the user, librarian pane, 27 Nov 2026 21:40): the sweep of the playbook's own pages is committed. That covers LB-Q6's three process pages, the home page, request journeys, and the seat names in `standards.md` and `change-a-standard.md` (`architect`, `librarian`; architect checked them 21:39, clear). Architect will flag two lines of `change-a-standard.md` that move to heimdall when Security's sections leave CONSTANTS (PA-Q126).
- CS-Q109 (b) (the operator, lead pane, 27 Nov 2026 22:57: "the other diagrams would follow, each in its own owner's ticket", relayed by the lead 23:24): the playbook's `platform` and `deploy-flow` diagrams are redrawn to src's `docs/diagram-conventions.md` once that page merges. The tier is `vg`, and the render goes to the operator before the commit.
- LB-Q9, "yes" (the user, librarian pane, 27 Nov 2026 23:32): the playbook's four citations of CONSTANTS "Exposure" now name `SECURITY.md` "Exposure", which holds the rule since PA-Q126 (src c63fa2c3). Tier `docs`.
- LB-Q10, "LB-Q10 yes" (the user, librarian pane, 27 Nov 2026 23:58): the `platform` and `deploy-flow` diagrams are redrawn to src's diagram conventions (74d61193, reladraw 0.16.0), under CS-Q109 (b). On the way, after these words:
  - "these dotted lines should not cross each other" (no time stamp on that message; it came after 23:42 and before 23:50): `zulip-state` moved below `zulip-server`;
  - "all the disk dotted lines could, and therefore should, be straight" (23:50): tried without the project box;
  - "restore the previous version, the box for the project was good to have" (23:53): the box kept. The `net-state` and `sylve-state` lines bend, because reladraw 0.16.0 aligns a node only with its siblings; architect adds this to the conventions page with SH-Q120.
