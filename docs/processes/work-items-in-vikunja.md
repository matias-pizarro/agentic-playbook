# Work items in Vikunja

_Intent, being built since 17 Nov 2026._ How the team's work items move from markdown files into production Vikunja, and what that adds to the platform. The decision is ADR-0010 (`docs/adr/0010-work-items-live-in-vikunja-with-a-database-audit-log.md` in src at `19c0bd8`); the design is the spec (`.scratch/vikunja-workflow/spec.md`, same commit); the rules for agents will be `docs/agents/issue-tracker.md`, rewritten for Vikunja (the spec's item 8). This page summarises them and links nothing it would restate.

## What

- **Work items become Vikunja tasks.** A task's description holds what to build, its requirements, the Ceremony line, its acceptance criteria and failure modes; its bucket, labels and links hold its state. Operators work in Vikunja's web UI; agents through Pi's MCP, and a small REST command for attachments.
- **Agents reach Vikunja only.** A WireGuard peer of their own, `vikunja-agents` at 10.131.0.4, always up on the host, routes only 10.130.1.10; the bastion lets it reach nothing else. The deploy peer `agents` (the interface `agentic`) stays for deploys ([CONSTANTS.md](../../imported/infra/CONSTANTS.md) "Deploys into the private network").
- **Over TLS, with a public certificate.** Caddy on the bastion obtains Vikunja's certificate for `vikunja.dkl.cat` on port 80, the one exception to "no web port" ([CONSTANTS.md](../../imported/infra/CONSTANTS.md) "Exposure"); relayd on vikunja-server serves 10.130.1.10:443 to the two peers only; clients resolve `vikunja.dkl.cat` to 10.130.1.10 by a hosts entry.
- **An audit log.** Database triggers record every change to tasks, comments, labels, links, buckets and attachments in a schema Vikunja's own role cannot alter, so a weakened acceptance criterion cannot pass unseen (rule 14). How to read it will be in Vikunja's README, under Infrastructure.

## Who does what

| Part | Who | Ticket |
|---|---|---|
| Projects, buckets, labels, the bot `agents-jail` and its token | the operator | 01 |
| The agents' Vikunja peer | prod-net, then the operator's host steps | 02 |
| Caddy and port 80 on the bastion | prod-net | 03 |
| TLS on vikunja-server; copying the certificate | prod-vikunja, the operator | 04 |
| The audit log | prod-vikunja | 05 |
| Pi's MCP access, the attachment command | vikunja-workflow | 06 |
| The ticket DAG read from Vikunja | vikunja-workflow | 07 |
| Moving the open work into Vikunja | the lead and the seats | 09 |

## Why

- One board for all open work, filterable by component, effort and importance, readable by an operator outside the agents' jail; statuses no longer drift in files (the spec's problem statement).
- Vikunja was already in production, private; this gives it users and rules (ADR-0010).
- The agents' path to Vikunja is narrower than their deploy path: one address, always up, while `agentic` reaches the whole network only for a deploy.

## Until a certificate service exists

Caddy renews the certificate on the bastion; the operator copies it to vikunja-server by hand after each renewal, about every 60 days, and port 80 stays open. A service that opens port 80 only around a renewal and distributes the certificate is in the backlog.
