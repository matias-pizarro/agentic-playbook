# Setting up the ACME validation zone

Your steps, done once: `cecinestpasundomaine.de` becomes the zone that answers Let's Encrypt's DNS-01 challenge for `vikunja.dkl.cat`, alone in a Hetzner project of its own, with a token that reaches nothing else ([CONSTANTS.md](../../imported/infra/CONSTANTS.md), "Certificates"; Vikunja task 138, DNS-01 1/3). Why this design, and what a stolen token could do: the findings of task 137, `.scratch/prod-architect/research-dns01.md` in src. The domain carries nothing else (the user, PA-Q84, "use cecinestpasundomaine.de", 18 Nov 02:17).

Steps 1 to 4 are yours, in the Hetzner Console and at the registrar. Steps 5 to 7 are reads prod-architect runs from the agents' jail once you give it the token; prod-architect reads each output as yes or no, and a command's error or an empty DNS answer as failed, never as no.

Read 18 Nov 02:20 at DENIC: the domain's name servers are already `ns1.your-server.de`, `ns3.second-ns.de` and `ns.second-ns.com`, with "Status: failed": DENIC checks that the name servers answer for the zone, and no zone exists at Hetzner yet. Step 2 creates it; step 3 has the registrar try again.

1. **Create the project `certificates-acme`** in the Hetzner Console (PA-Q82). It holds the zone and nothing else.
2. **Create the zone `cecinestpasundomaine.de`** in that project, as a primary zone, labelled `component=certificates-acme`, with no records of your own. Its "Name servers" tab lists the name servers it answers on ([Hetzner, Updating name servers](https://docs.hetzner.com/networking/dns/getting-started/delegate-to-hetzner/)); they should be the three above.
3. **Have the registrar submit the name servers again**, as listed in step 2, in that order. A change can take up to 48 hours to propagate (same page).
4. **Create a read-write API token** in the project (Security, API tokens), and **set a cost alert** on the project: it emails you about spending there, though it does not stop it. Put the token in `~/.config/sandbox/acme-zone.token` on the host, mode 600, and tell prod-architect it is there. The token never goes into a repository, a pane or a message.
5. `whois -h whois.denic.de cecinestpasundomaine.de`: yes when it says `Status: connect`.
6. `drill cecinestpasundomaine.de NS`: yes when the answer lists exactly the name servers of step 2.
7. `HCLOUD_TOKEN=$(cat ~/.config/sandbox/acme-zone.token) hcloud all list`: yes when it lists the zone `cecinestpasundomaine.de` and nothing else; the token's project holds nothing a stolen token could already be using.

**If it fails:** each step can be done again, and nothing in production depends on it yet: `vikunja.dkl.cat` keeps the certificate Caddy obtained on the bastion, valid until 14 Feb 2027.
