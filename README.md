# Production playbook

How production is built and kept running: the Hetzner Cloud project `agentic-workflows`, Phase 1a (net), 1b (vikunja), 1c (sylve) and later phases. Its architecture, processes and technical details, and the resources catalog.

- **Architecture, Processes, Technical details**: written by seat `prod-architect`.
- **Infrastructure (from src)**: the infra READMEs and `infra/CONSTANTS.md`, imported from src at the commit `docs-site/mkdocs.yml` names (`extra.src_commit`). Their code and rules live in src; each such page names its commit.
- **Resources catalog**: to come, once Phase 1a is in production; generated from the project by src's `infra/net/catalog`.

The playbook names where each secret lives and never holds one.

## Serve it

Run from the repo root; each command is safe to rerun.

1. `uv sync`: makes `.venv` with the site's tools.
2. `.venv/bin/pre-commit install`: installs the hooks (gitleaks among them; needs `pkg install gitleaks`).
3. `rm -rf imported && mkdir imported && git -C ../src archive "$(sed -n 's/^  src_commit: //p' docs-site/mkdocs.yml)" infra | tar -x -C imported --include='*.md'`: imports the infra pages at the named src commit into `imported/`, which git ignores.
4. `uv run mkdocs build --strict -f docs-site/mkdocs.yml -d "$(git rev-parse --show-toplevel)-site"`: builds the site beside the repo, failing on any warning (`-d` resolves from the config's directory, so it is given in full).
5. `uv run mkdocs serve -f docs-site/mkdocs.yml`: serves it at <http://127.0.0.1:8000>.

The export `NO_MKDOCS_2_WARNING=true DISABLE_MKDOCS_2_WARNING=true` silences the MkDocs 2.0 banners, as in src.

## Writing here

Each writer works on a `feat/<topic>` branch in its own worktree; seat `prod-playbook` merges into `main` with `git merge --no-ff` once the strict build passes on the branch. A new page needs a line in `docs-site/nav.md`, added in the same commit: the strict build fails on a page missing from the nav, and on a nav glob matching nothing.
