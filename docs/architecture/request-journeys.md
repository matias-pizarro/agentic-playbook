# Request journeys

How an incoming request travels through the network, and how a certificate is renewed. Plain arrows are `vikunja.dkl.cat`, as it runs today. Each orange band, just below an arrow, is the same step for `zulip.dkl.cat`, as decided but not yet built (PA-Q122; Vikunja tasks 194 and 195).

## A user's request

Everything is on the private network. The only door from the internet is WireGuard on the bastion. A peer's own address is kept as far as `sylve-server`, so each layer filters by who it really is ([SECURITY.md](../../imported/infra/SECURITY.md), "Exposure", and [CONSTANTS.md](../../imported/infra/CONSTANTS.md), "Deploys into the private network").

```mermaid
sequenceDiagram
    autonumber
    participant P as Phone (mlp_phone 10.131.0.5)
    participant D as Hetzner DNS (zone dkl.cat)
    participant B as net-bastion (10.130.0.2)
    participant S as sylve-server (alias 10.130.1.10)
    participant X as proxy jail (10.132.0.5, nginx)
    participant V as vikunja jail (10.132.0.10:3456)
    participant G as pgprimary jail (10.132.0.20)
    participant Z as zulip-server (10.130.1.12)
    P->>D: vikunja.dkl.cat A?
    rect rgba(255, 140, 0, 0.25)
    P->>D: zulip.dkl.cat A?
    end
    D-->>P: 10.130.1.10, a public record for a private address
    rect rgba(255, 140, 0, 0.25)
    D-->>P: 10.130.1.10 too, the same front address
    end
    P->>B: TLS to 10.130.1.10:443 inside WireGuard, UDP 51820
    rect rgba(255, 140, 0, 0.25)
    P->>B: the same, the same peer and port, so no bastion change
    end
    Note over B: pf holds mlp_phone to 10.130.1.10:443 only<br/>no NAT, the source stays 10.131.0.5
    B->>S: routed on net-network, Hetzner sends the alias to sylve-server
    rect rgba(255, 140, 0, 0.25)
    B->>S: the same
    end
    Note over S: pf lets 443 in from Vikunja's tls_peers only<br/>and redirects it to the proxy jail's port 8443
    S->>X: TLS, SNI vikunja.dkl.cat
    rect rgba(255, 140, 0, 0.25)
    S->>X: TLS, SNI zulip.dkl.cat, on the same port
    end
    Note over X: TLS ends here, nginx picks the certificate by SNI
    X->>V: plain HTTP on the jails' internal bridge
    rect rgba(255, 140, 0, 0.25)
    X->>Z: HTTPS to 10.130.1.12:443, leaving sylve-server as 10.130.1.11<br/>Zulip's nftables lets 443 in from 10.130.1.11 only
    end
    V->>G: SQL, pg_hba lets in the Vikunja jail only
    rect rgba(255, 140, 0, 0.25)
    Z->>Z: Zulip and its own PostgreSQL, on its LUKS disk
    end
    V-->>X: response
    rect rgba(255, 140, 0, 0.25)
    Z-->>X: response
    end
    X-->>P: HTTPS response, back the same way
    rect rgba(255, 140, 0, 0.25)
    X-->>P: the same
    end
```

Sylve's UI follows the Vikunja journey to 10.130.1.11:443, from Sylve's peers, to the proxy's port 443. The agents reach both names the same way, from `vikunja-agents` (10.131.0.4).

## A certificate renewal (DNS-01)

Nothing comes into the network. Every connection goes outward through the NATs, and Let's Encrypt checks only public DNS at Hetzner. Port 80 is closed ([SECURITY.md](../../imported/infra/SECURITY.md), "Exposure", and [CONSTANTS.md](../../imported/infra/CONSTANTS.md), "Certificates").

```mermaid
sequenceDiagram
    autonumber
    participant L as lego in the proxy jail, daily cron
    participant N as sylve-server then net-bastion, NAT out
    participant LE as Let's Encrypt ACME API
    participant H as Hetzner DNS API, project certificates-acme
    participant NS as Hetzner name servers
    L->>N: HTTPS out, no inbound port is used
    N->>LE: new order for vikunja.dkl.cat
    rect rgba(255, 140, 0, 0.25)
    N->>LE: new order for zulip.dkl.cat
    end
    LE-->>L: challenge, a TXT at _acme-challenge.vikunja.dkl.cat
    rect rgba(255, 140, 0, 0.25)
    LE-->>L: challenge, a TXT at _acme-challenge.zulip.dkl.cat
    end
    L->>H: create the TXT at _acme-challenge.vikunja.cecinestpasundomaine.de<br/>with the validation zone's token, which cannot reach production
    rect rgba(255, 140, 0, 0.25)
    L->>H: create the TXT at _acme-challenge.zulip.cecinestpasundomaine.de, the same token
    end
    L->>NS: wait until ns1.your-server.de answers the CNAME and the TXT
    rect rgba(255, 140, 0, 0.25)
    L->>NS: the same for zulip
    end
    L->>LE: ready
    LE->>NS: _acme-challenge.vikunja.dkl.cat?
    rect rgba(255, 140, 0, 0.25)
    LE->>NS: _acme-challenge.zulip.dkl.cat?
    end
    NS-->>LE: CNAME to _acme-challenge.vikunja.cecinestpasundomaine.de, then its TXT
    rect rgba(255, 140, 0, 0.25)
    NS-->>LE: CNAME to _acme-challenge.zulip.cecinestpasundomaine.de, then its TXT
    end
    LE-->>L: valid, the certificate is issued
    rect rgba(255, 140, 0, 0.25)
    LE-->>L: valid, the certificate is issued
    end
    L->>H: delete the TXT
    rect rgba(255, 140, 0, 0.25)
    L->>H: delete the TXT
    end
    Note over L: the certificate and key go to the jail's encrypted dataset and nginx reloads<br/>a failure is mailed to root, which nobody reads, see the backlog
```

The CNAME in `dkl.cat` is the delegation. A stolen validation-zone token can obtain certificates for the delegated names, but it touches no production resource.
