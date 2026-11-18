# Setting up docbase.com as the ACME validation zone

Your steps, done once: `docbase.com` becomes the zone that answers Let's Encrypt's DNS-01 challenge for `vikunja.dkl.cat`, alone in a Hetzner project of its own, with a token that reaches nothing else ([CONSTANTS.md](../../imported/infra/CONSTANTS.md), "Certificates"; Vikunja task 138, DNS-01 1/3). Why this design, and what a stolen token could do: the findings of task 137, `.scratch/prod-architect/research-dns01.md` in src.

Steps 1 to 5 are yours, in the Hetzner Console and at the registrar. Steps 6 to 8 are reads prod-architect runs from the agents' jail once you give it the token; each prints yes, no or failed, and a failed read is never taken as no. `docbase.com`'s own site (A 188.40.142.13) stops answering between steps 2 and 4; you accepted that (PA-Q81).

Today (read 18 Nov 02:05) `docbase.com` is registered with Hetzner Online GmbH and served by Hetzner's older DNS: `ns1.first-ns.de`, `robotns2.second-ns.de`, `robotns3.second-ns.com`.

1. **Create the project** in the Hetzner Console, named as PA-Q82 settles. It holds `docbase.com`'s zone and nothing else.
2. **Remove `docbase.com` from the older DNS** (where it is kept today, the Robot or konsoleH DNS administration): Hetzner refuses to create a zone "already claimed by somebody else" until the older one is gone ([Hetzner, DNS FAQ: Zones](https://docs.hetzner.com/networking/dns/faq/zones/)). Note its records first if any should come back.
3. **Create the zone `docbase.com`** in the new project, as a primary zone, with no records of your own. Its "Name servers" tab lists the name servers to set at the registrar ([Hetzner, Updating name servers](https://docs.hetzner.com/networking/dns/getting-started/delegate-to-hetzner/)).
4. **Set the registrar's name servers** for `docbase.com` to those of step 3, in the order shown. A change can take up to 48 hours to propagate (same page).
5. **Create a read-write API token** in the new project (Security, API tokens), and **set a cost alert** on the project. Put the token in `~/.config/sandbox/docbase-acme.token` on the host, mode 600, and tell prod-architect it is there. The token never goes into a repository, a pane or a message.
6. `drill docbase.com NS`: yes when the answer lists exactly the name servers of step 3.
7. `HCLOUD_TOKEN=$(cat ~/.config/sandbox/docbase-acme.token) hcloud zone list -o noheader -o columns=name`: yes when it prints `docbase.com` alone.
8. With the same token, `hcloud server list`, `hcloud volume list`, `hcloud primary-ip list` and `hcloud load-balancer list`: yes when each prints nothing; the token's project holds the zone and nothing else.

**If it fails:** each step can be done again. Until step 4 is read yes, `vikunja.dkl.cat` keeps its HTTP-01 certificate from Caddy on the bastion, valid until 14 Feb 2027, and nothing in production changes.
