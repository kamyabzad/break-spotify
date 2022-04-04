import sys

import dns.resolver
import pyperclip

SHECAN_NAMESERVRES = ["178.22.122.100", "185.51.200.2"]
SPOTIFY_DOMAIN = "spotify.com"
SPOTIFY_HOSTS = [
    "accounts.spotify.com",
    "api-partner.spotify.com",
    "api.spotify.com",
    "dealer.spotify.com",
    "open.spotify.com",
    "partners.wg.spotify.com",
    "spclient.wg.spotify.com",
    "www.spotify.com",
]

if __name__ == "__main__":
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = SHECAN_NAMESERVRES

    answer = resolver.resolve(SPOTIFY_DOMAIN)
    if not len(answer):
        print(f"Couldn't resolve {SPOTIFY_DOMAIN}")
        sys.exit()

    proxy_ip = str(answer[0])

    s = "\n".join(f"{proxy_ip:<16}{host}" for host in SPOTIFY_HOSTS)

    print(
        f"Add the following lines to your `/etc/hosts`. (It's copied to your clipboard)\n\n{s})"
    )
    pyperclip.copy(s)
