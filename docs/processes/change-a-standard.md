# Changing a standard, and review before merge

How the rules in [CONSTANTS.md](../../imported/infra/CONSTANTS.md) "Production" change, and how each component's work is checked against them. Seat `prod-architect` keeps the components in step; the user decides.

## A rule changes

1. A seat, or prod-architect's review, finds that a rule is missing, wrong, or read two ways. The seat asks in its own pane or reports to the lead; prod-architect puts it to the user as one question in its pane, with each seat's position, the options with their effort and tradeoffs, and a recommendation.
2. The user answers in prod-architect's pane.
3. prod-architect writes the rule into `infra/CONSTANTS.md` on its branch, quoting the user's words and time, and merges it on the lead's authorisation. No other seat edits the production rules, so they never conflict.
4. The lead relays the decision to the seats it touches; each merges integration into its branch and applies it.

## Review before merge

prod-architect reads a component's work, never changes it, at two points:

- **its perimeter or ticket**, before code: the cheapest point to catch a divergence;
- **its branch before the merge into integration**: names, labels, addresses, keys and access, protection, the catalog, the conf, the scripts' shape, the README's four parts, and what the component gives and needs from the others.

Each finding goes to the user in prod-architect's pane. A finding between components, or a README missing a part, holds the merge until the user answers it; "backlog" releases it. The seat's own code review, on a different model, remains the review of its code.
