# Standards

What every production component follows, where it is written, and how it changes.

## Where the standards live

| What | Where | Who writes it |
|---|---|---|
| Rules a production script applies: labels, names, addresses, access, protection, files on the host, documentation | src `infra/CONSTANTS.md`, section "Production" ([imported](../../imported/infra/CONSTANTS.md)) | seat `prod-architect`, each rule quoting the user's decision |
| How scripts are written | src `CODING_STANDARDS.md` | any seat, by review |
| The vocabulary | src `GLOSSARY.md`, and this site's [Glossary](../../GLOSSARY.md) | prod-architect for production terms |
| Decisions that are hard to reverse | src `docs/adr/` | the seat making the decision |
| How production is run | this playbook | each component its README; prod-architect the cross-component pages |

The playbook links to a rule; it never restates one, so there is one place to change it (PA-Q4).

## Each component's README

Every component documents itself in `infra/<component>/README.md` in src, which the playbook imports (PA-Q37), in four parts (PA-Q38):

1. **What**: its purpose, its resources, what it gives the other components and what it needs from them.
2. **Why**: each decision that shapes it, one sentence each, linking where it was decided.
3. **How**: deploy, verify, operate, replace, and the user's own steps, each a command run live.
4. **State and recovery**: what survives a rebuild, where it lives, what is lost with the cloud disk.

An architecture diagram and a functional diagram go with it where they apply, in reladraw. A component not yet built writes its intent in the same shape, marked as intent. A README missing a part holds the component's merge until the user answers the finding (PA-Q39).

## How a standard changes

See [Changing a standard](../processes/change-a-standard.md).
