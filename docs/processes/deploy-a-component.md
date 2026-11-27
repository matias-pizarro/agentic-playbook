# Deploying a component

How any component's server joins the private network, in the order every component follows. The commands are in each linked page, run live there; this page says who does what, and why in that order.

| Step | Who | What | Why |
|---|---|---|---|
| 1 | the user | gives the seat the go for the spend, in its pane, and keeps the read-write token in place | nothing is created in production without it |
| 2 | the user | brings the agents' tunnel up on the host: `wg-quick up prod-agt-deploy` ([CONSTANTS.md](../../imported/infra/CONSTANTS.md) "Deploys into the private network") | the agents' jail reaches the network only through it |
| 3 | the seat | creates its server on `net-network` at its fixed address, without a public address, with every `role=admin` key ([net's README](../../imported/infra/net/README.md) "Attaching a server") | the address and name come from CONSTANTS' table |
| 4 | the seat | names it: a record set `<component>.private` in `dkl.cat`, labelled with its component | a component adds to net's zone only through its own labelled record set |
| 5 | the seat | installs and runs its live checks over ssh through the tunnel | live before protection: a failed run can still be thrown away |
| 6 | the seat | turns on protection, once the live checks pass; a resource recreated later is protected as it is created ([CONSTANTS.md](../../imported/infra/CONSTANTS.md) "Protection") | a failed first deploy can still be thrown away; a protected resource no longer can (PA-Q42) |
| 7 | the seat | writes the catalog again: `infra/net/catalog infra/net/prod.conf` (net's README) | the catalog shows production as it stands |
| 8 | the user | brings the tunnel down, `wg-quick down prod-agt-deploy`, and deletes the read-write token in the Console | while the tunnel is up, everything on the host reaches the network; the token is needed only to deploy |

A server is replaced the same way, after the user turns its protection off and deletes it; its cloud disk, and so its state, stays.
