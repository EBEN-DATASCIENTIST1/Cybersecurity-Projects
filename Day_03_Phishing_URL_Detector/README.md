# Day 3 — Phishing URL Detector

## Overview

This project is a Python-based tool that analyzes URLs for indicators commonly associated with phishing attacks. It assigns a heuristic risk score between 0 and 100 and explains the indicators detected.

The objective is to learn how suspicious URL characteristics can be identified programmatically. This project builds a detector, not a phishing page.

## Features

- Analyze a single URL or a list of sample URLs.
- Detect suspicious keywords such as `login`, `verify`, `bank`, and `paypal`.
- Flag URLs using HTTP instead of HTTPS.
- Identify IP addresses used as hostnames.
- Detect `@` characters that can obscure the actual destination.
- Flag hostnames containing punycode.
- Assign LOW, MEDIUM, HIGH, or CRITICAL risk levels.
- Explain the indicators contributing to each score.
- Save batch results to a text report.

## Technologies Used

- Python
- `re` — regular expressions
- `urllib.parse` — URL parsing
- `pathlib` — file and report handling

No third-party packages are required.

## Installation

Install Python 3.11 or a compatible version. No additional Python packages are required.

## Usage

Run the program from the project directory:

```bash
python main.py
```

Choose option 1 to analyze a single URL or option 2 to analyze all URLs in `data/sample_urls.txt`.

Batch results are saved to `reports/phishing_report.txt`.

## Scoring Rules

The detector adds points when it finds suspicious URL characteristics:

- HTTP instead of HTTPS: 20 points
- Suspicious keywords: 10 points per keyword, up to 30 points
- Many hostname components: 15 points
- `@` symbol in the URL: 20 points
- IP address used as the hostname: 25 points
- Punycode in the hostname: 20 points

The maximum score is 100.

## Risk Classification

- **LOW:** 0–19 points
- **MEDIUM:** 20–39 points
- **HIGH:** 40–69 points
- **CRITICAL:** 70–100 points

These scores are heuristic indicators, not proof that a URL is malicious. Legitimate websites can trigger warnings, and malicious URLs may evade detection.

## Testing

The sample dataset contains 10 URLs covering ordinary domains and suspicious indicators.

The detector successfully processed all 10 sample URLs and generated a text report.

## Limitations

- Scores are heuristic indicators, not probabilities or definitive phishing verdicts.
- Legitimate websites may trigger warnings.
- Phishing URLs may evade these simple rules.
- HTTPS does not guarantee that a website is trustworthy.
- Punycode is also used by legitimate internationalized domain names.
- The tool does not inspect website content, certificates, domain reputation, or live threat intelligence.

## Ethical Use

Use this tool for education and defensive security analysis. Do not use it to create phishing pages, steal credentials, or facilitate unauthorized attacks.
