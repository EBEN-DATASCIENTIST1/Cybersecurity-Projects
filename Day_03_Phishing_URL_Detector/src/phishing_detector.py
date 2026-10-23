
import re
from urllib.parse import urlparse

KEYWORDS = {
    "login", "verify", "secure", "update",
    "account", "bank", "paypal", "password"
}


def phish_score(url):
    score = 0
    reasons = []

    parsed = urlparse(url.strip())
    hostname = (parsed.hostname or "").lower()

    # 1. Validate URL structure
    if parsed.scheme not in {"http", "https"} or not hostname:
        return 100, ["Invalid or unsupported URL format"]

    # 2. Check HTTPS
    if parsed.scheme != "https":
        score += 20
        reasons.append("Uses HTTP instead of HTTPS")

    # 3. Check suspicious keywords in hostname and path
    text_to_check = hostname + parsed.path.lower()
    found_keywords = sorted(
        keyword for keyword in KEYWORDS
        if keyword in text_to_check
    )

    if found_keywords:
        score += min(10 * len(found_keywords), 30)
        reasons.append(
            "Contains suspicious keywords: "
            + ", ".join(found_keywords)
        )

    # 4. Check excessive subdomains
    if len(hostname.split(".")) >= 5:
        score += 15
        reasons.append("Contains many hostname components")

    # 5. Check '@' in the URL
    if "@" in url:
        score += 20
        reasons.append("Contains '@', which can obscure the destination")

    # 6. Check IP address used as hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        score += 25
        reasons.append("Uses an IPv4 address instead of a domain name")

    # 7. Check punycode, often used in internationalized domains
    if "xn--" in hostname:
        score += 20
        reasons.append("Hostname contains punycode")

    score = min(score, 100)

    if not reasons:
        reasons.append("No configured warning indicators detected")

    return score, reasons
