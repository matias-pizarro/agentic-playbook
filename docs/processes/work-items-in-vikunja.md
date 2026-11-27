# Work items in Vikunja

The team's work items are tasks in production Vikunja, at `https://vikunja.dkl.cat/`. The decision is ADR-0010 in src (`docs/adr/0010-work-items-live-in-vikunja-with-a-database-audit-log.md`).

## What

- **A work item is a Vikunja task.** Its description holds what to build, its requirements, the Ceremony line, its acceptance criteria and its failure modes. Its bucket, labels and links hold its state.
- **The user works in Vikunja's web UI.** Each seat works through Pi's Vikunja MCP, as a bot of its own, whose token `operator-setup.sh <seat>` makes on the host. Until a seat has its bot, it uses the shared bot `bot-agents-jail`.
- **Reached over WireGuard only, by HTTPS.** The agents' peer `vikunja-agents` (10.131.0.4) is always up and is held by the bastion to 10.130.1.10:443. The reverse proxy there serves `vikunja.dkl.cat` with a Let's Encrypt certificate ([Architecture](../architecture/overview.md); [CONSTANTS.md](../../imported/infra/CONSTANTS.md) "Exposure").
- **An audit log.** Database triggers record every change to tasks, comments, labels, links, buckets and attachments, in a schema Vikunja's own database role cannot alter. A weakened acceptance criterion therefore cannot pass unseen (rule 14). How to read it is in Vikunja's README, under Infrastructure.

## Why

- One board for all open work, filterable by component, effort and importance, and readable by the user outside the agents' jail. Statuses no longer drift in files (ADR-0010).
- The agents' path to Vikunja is narrower than their deploy path: one address and one port, always up, while `prod-agt-deploy` reaches the whole network only during a deploy.
