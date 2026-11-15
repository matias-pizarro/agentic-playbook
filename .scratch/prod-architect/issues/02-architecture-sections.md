Ceremony: checklist (the user, "PA-Q31,32,34,35,36,37,38,39,40: yes", 15 Nov 2026 23:46)

# 02: the playbook's cross-component sections

**What to build:** seat `prod-architect`'s sections of the playbook (PA-Q17), what spans components only (PA-Q40): Architecture (how the components fit and why, with an architecture diagram, a functional deploy diagram, and the intent for 1b, 1c and Phase 2 with its diagram, PA-Q33 B), Standards (where the standards live, the README shape, PA-Q37 to PA-Q39), and the Processes that span components (deploying a component, changing a standard and review before merge). Each component's own what, why and how is its README, imported from src.

**Blocked by:** None

**Status:** in-progress

## Commands

Run from the worktree's root.

1. `rm -rf imported && mkdir imported && git -C ../../src archive "$(sed -n 's/^  src_commit: //p' docs-site/mkdocs.yml)" infra | tar -x -C imported --include='*.md'`: imports the infra pages the new pages link to.
2. `reladraw docs/architecture/<name>.reladraw` for `platform`, `deploy-flow`, `phase-2`: writes each SVG beside its source.
3. `uv run mkdocs build --strict -f docs-site/mkdocs.yml -d /tmp/pa-site`: the strict build; fails on any warning.
4. `uv run mkdocs serve -f docs-site/mkdocs.yml -a 127.0.0.1:8001`: the render the user sees before the commit (PA-Q35; 8000 is the main checkout's).

**If it fails:** nothing outside this branch changes; fix the page or the diagram and rebuild.

## Comments

### 2026-11-16

- The render (127.0.0.1:8001, PDFs) approved: the user, PA-Q45, "yes" (00:46). Since the render: step 6 of the deploy page states PA-Q42's answer (same message), and the agents' interface is `agentic` (00:37).
