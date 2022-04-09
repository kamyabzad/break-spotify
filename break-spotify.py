import platform
import sys

import dns.resolver
import pyperclip

SYSTEM = platform.system()
PLATFORMS_HOSTS = {
    "Linux": "/etc/hosts",
    "Darwin": "/etc/hosts",
    "Windows": "c:\Windows\System32\Drivers\etc\hosts",
}

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

    hosts_string = "\n".join(f"{proxy_ip:<16}{host}" for host in SPOTIFY_HOSTS)
    platform_help_string = (
        f"Copy the following lines to your `{PLATFORMS_HOSTS[SYSTEM]}`"
        if PLATFORMS_HOSTS.get(SYSTEM)
        else "(Couldn't recognize hosts file for this platform)"
    )

    pyperclip.copy(hosts_string)
    print(
        (
            "Hosts generated and copied to your clipboard.\n"
            f"  Platform: {SYSTEM}\n"
            f"  {platform_help_string}\n\n"
            f"{hosts_string}"
        )
    )
