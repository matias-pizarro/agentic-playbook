Ceremony: checklist (the user, "PP-Q15,16,17,18: yes", 15 Nov 2026 22:50)

# 01: the playbook's site, served locally

**What to build:** this repo as a Material for MkDocs site set up as src's (PP-Q13), named "Production playbook", served on this machine; the infra READMEs and `CONSTANTS.md` imported from src at the commit `docs-site/mkdocs.yml` names (`extra.src_commit`), each imported page saying so; empty sections for prod-architect. Decisions: [the perimeter](../perimeter.md).

**Blocked by:** None

**Status:** done (the catalog page waits in the backlog for net's Phase 1a merge)

## Commands

Run from the repo root. The README lists 3 to 5 for everyday use.

1. `uv sync`: makes `.venv` with MkDocs Material 9.7.7, literate-nav, pre-commit and commitizen from `pyproject.toml`.
2. `.venv/bin/pre-commit install`: installs the hooks, gitleaks among them (PP-Q6).
3. `rm -rf imported && mkdir imported && git -C ../src archive "$(sed -n 's/^  src_commit: //p' docs-site/mkdocs.yml)" infra | tar -x -C imported --include='*.md'`: imports the infra pages at the named src commit into `imported/`, which git ignores (PP-Q7).
4. `uv run mkdocs build --strict -f docs-site/mkdocs.yml -d "$(git rev-parse --show-toplevel)-site"`: builds the site beside the repo, failing on any warning; imported pages' links to src files the playbook lacks become plain text (`docs-site/hooks.py`, PP-Q19).
5. `uv run mkdocs serve -f docs-site/mkdocs.yml`: serves it at http://127.0.0.1:8000 on this machine (PP-Q9, PP-Q15).

Verified by running 1 to 5 here and showing the user a render before the commit (rule 9).

**If it fails:** the failing command prints why; fix it and rerun from that command, since each is safe to rerun.
