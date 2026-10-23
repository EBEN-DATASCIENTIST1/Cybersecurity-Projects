
import socket
import requests
import whois
from pathlib import Path
from src.dns_analyzer import analyze_dns
import re


def is_valid_domain(domain):
    domain = domain.strip().rstrip(".")

    if len(domain) > 253:
        return False

    labels = domain.split(".")

    if len(labels) < 2:
        return False

    for label in labels:
        if not re.fullmatch(
            r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?",
            label
        ):
            return False

    return True


def osint_scan(domain):
    # Keep your existing scanner code here
    ...


def osint_scan(domain):
    # Create the reports folder
    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    # Create the report file
    report_file = report_dir / f"{domain}.txt"
    report = []

    def log(message=""):
        print(message)
        report.append(str(message))

    log("=" * 45)
    log(f"OSINT REPORT: {domain}")
    log("=" * 45)

    # 1. WHOIS lookup
    log("\n[WHOIS]")

    try:
        info = whois.whois(domain)

        log(f"Registrar: {info.registrar or 'Not available'}")
        log(f"Creation date: {info.creation_date or 'Not available'}")
        log(f"Expiry date: {info.expiration_date or 'Not available'}")

    except Exception as error:
        log(f"WHOIS lookup unavailable: {error}")
        log("Continuing with the other OSINT checks...")

    # 2. DNS resolution
    try:
        ip = socket.gethostbyname(domain)

        log("\n[DNS]")
        log(f"IP address: {ip}")

    except socket.gaierror as error:
        log(f"\nDNS resolution failed: {error}")

        report_file.write_text(
            "\n".join(report),
            encoding="utf-8"
        )
        log(f"Report saved to: {report_file}")
        return

    # 3. IP geolocation
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            params={
                "fields": "status,message,country,regionName,city,isp"
            },
            timeout=10
        )

        response.raise_for_status()
        geo = response.json()

        log("\n[IP GEOLOCATION]")

        if geo.get("status") == "success":
            log(f"Country: {geo.get('country')}")
            log(f"Region: {geo.get('regionName')}")
            log(f"City: {geo.get('city')}")
            log(f"ISP: {geo.get('isp')}")
        else:
            log(
                "Geolocation lookup failed: "
                f"{geo.get('message', 'Unknown error')}"
            )

    except requests.RequestException as error:
        log(f"Geolocation request failed: {error}")

       
    # 4. DNS record analysis
    log("\n[DETAILED DNS ANALYSIS]")

    dns_results = analyze_dns(domain)

    for record_type, records in dns_results.items():
        log(f"\n[{record_type} RECORDS]")

        if records:
            for record in records:
                log(record)
        else:
            log("No records found or lookup failed.")
