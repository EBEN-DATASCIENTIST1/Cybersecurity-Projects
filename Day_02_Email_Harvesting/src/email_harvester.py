
import re
from pathlib import Path
import requests


EMAIL_PATTERN = (
    r"\b[A-Za-z0-9._%+-]+@"
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def harvest_emails(html):
    return set(
        re.findall(EMAIL_PATTERN, html, re.IGNORECASE)
    )


def harvest_from_file(file_path):
    path = Path(file_path)
    html = path.read_text(encoding="utf-8")
    return harvest_emails(html)


def harvest_from_url(url):
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "EducationalEmailHarvester/1.0"}
    )
    response.raise_for_status()
    return harvest_emails(response.text)
