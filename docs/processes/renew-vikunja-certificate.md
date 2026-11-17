# Renewing Vikunja's certificate

Caddy on the bastion renews the Let's Encrypt certificate for `vikunja.dkl.cat` about 30 days before it expires; hitch on Vikunja's server keeps serving the copy it loaded until the user copies the new one over. The current certificate expires on 14 Feb 2027, so Caddy renews it around 15 Jan 2027; then every 60 days or so. The steps come from [Vikunja's README](../../imported/infra/vikunja/README.md), How, step 5, and [net's README](../../imported/infra/net/README.md), "Vikunja's certificate"; those pages are the source if they differ.

Steps 1 to 4 run on your laptop, from a checkout of src, over your WireGuard tunnel, with your `role=admin` key. Step 4 is a deploy: it needs the read-write token in place, as for any deploy ([Deploying a component](deploy-a-component.md)). Steps 5 and 6 run in the agents' jail.

1. `ssh root@10.130.0.2 openssl x509 -noout -enddate -in /netstate/caddy/certificates/acme-v02.api.letsencrypt.org-directory/vikunja.dkl.cat/vikunja.dkl.cat.crt`: prints when the certificate Caddy holds expires. A later date than step 2's means Caddy has renewed it.
2. `ssh root@10.130.1.10 openssl x509 -noout -enddate -in /var/db/vikunja/tls/vikunja.dkl.cat.crt`: prints when the copy on Vikunja's server expires. The same date as step 1's means there is nothing to copy; stop here.
3. `d=/netstate/caddy/certificates/acme-v02.api.letsencrypt.org-directory/vikunja.dkl.cat && scp -3 root@10.130.0.2:$d/vikunja.dkl.cat.crt root@10.130.0.2:$d/vikunja.dkl.cat.key root@10.130.1.10:/var/db/vikunja/tls/`: copies the certificate and its key from the bastion straight to the server. The key passes through your laptop's memory, never its disk.
4. `infra/vikunja/up infra/vikunja/prod.conf`: checks the certificate (present, for `vikunja.dkl.cat`, matching its key, valid for more than a day), then restarts hitch on it. It stops and names the problem if any of those checks fails.
5. From the agents' jail, through the peer `vikunja-agents` (10.131.0.4): `echo | openssl s_client -connect 10.130.1.10:443 -servername vikunja.dkl.cat 2>/dev/null | openssl x509 -noout -enddate`. This prints when the served certificate expires, which should be step 1's date.
6. `infra/vikunja/check-tls infra/vikunja/prod.conf served`, from a src checkout in the jail: PASS on `/api/v1/info` with the certificate verified, PASS on MCP, PASS on 3456 closed.

**If it fails:** hitch keeps serving the certificate it last loaded until that one expires, or `up` stops it, naming the cause. Fix the cause and run the steps again from step 3.
