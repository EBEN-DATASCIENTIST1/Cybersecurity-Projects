# Day 1 — OSINT & Passive Reconnaissance

## Overview

This project is a beginner-friendly Python OSINT (Open-Source Intelligence) tool that collects publicly available information about a domain.

It performs WHOIS lookups, DNS resolution, detailed DNS record analysis, and IP geolocation.

## Features

- **WHOIS Lookup:** Retrieves domain registration information when available.
- **DNS Resolution:** Resolves a domain to an IP address.
- **IP Geolocation:** Retrieves approximate geographic and network information associated with an IP address.
- **DNS Record Analysis:** Retrieves A, AAAA, MX, NS, and TXT records.
- **Input Validation:** Rejects malformed domain names.
- **Report Generation:** Saves scan results as text files in the `reports/` directory.

## Technologies Used

- Python
- python-whois
- Requests
- dnspython
- Socket
- pathlib
- Regular expressions

## Project Structure

```text
Day_01_OSINT_Reconnaissance/
├── data/
├── reports/
├── screenshots/
├── src/
│   ├── __init__.py
│   ├── dns_analyzer.py
│   └── osint_scanner.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Install Python 3.11 or a compatible Python version.
2. Open a terminal in the project directory.
3. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program from the project root:

```bash
python main.py
```

Enter a domain when prompted. For example:

```text
example.com
```

The program attempts to collect WHOIS information, resolve the domain's IP address, retrieve IP geolocation data, and analyze DNS records.

The generated report is saved in the `reports/` directory.

## Limitations

- WHOIS servers may time out or return incomplete information.
- DNS records can change over time.
- IP geolocation is approximate and does not establish a website server's exact physical location.
- Results depend on network connectivity and the availability of external services.
- A missing DNS record does not necessarily indicate a security problem.

## Ethical Use

This project is intended for educational purposes and authorized passive reconnaissance.

Use it only to investigate domains you own or have permission to assess. It does not attempt to exploit systems, bypass access controls, or perform intrusive vulnerability testing.

## Learning Objectives

- Understand the fundamentals of OSINT.
- Learn how WHOIS and DNS work.
- Use Python libraries to retrieve public information.
- Handle network errors.
- Validate user input.
- Generate reports from security-related data.
