# Day 5 — OSINT + Social Engineering: Target Profile

## Overview

This project is a Python-based OSINT tool that collects publicly available information from GitHub profiles and generates a defensive exposure assessment.

It demonstrates how public profile information and repository metadata can be organized into a structured report to help users understand and reduce their digital exposure.

## Features

- Retrieve public GitHub profile information.
- Collect details about recent public repositories.
- Identify programming languages used in recent repositories.
- Export profile information to JSON.
- Review publicly exposed profile information.
- Generate a defensive threat assessment report.
- Handle network errors and GitHub API responses.

## Technologies Used

- Python
- Requests
- JSON
- pathlib

## Usage

Run the program from the project directory:

```bash
python main.py
```

Enter a GitHub username when prompted. Use your own account or an account you are authorized to assess.

The program retrieves available public profile information, analyzes basic exposure indicators, and generates two reports.

## Generated Reports

**1. `reports/github_profile.json`**

Contains the retrieved public profile information, including:

- Username and display name
- Public bio, company, and location fields when available
- Public repository count
- Programming-language counts for the retrieved repositories
- Details of recent public repositories

**2. `reports/threat_assessment.txt`**

Contains basic exposure findings and defensive recommendations, including reviewing public profile details, checking repositories for accidentally exposed secrets, enabling two-factor authentication, and reviewing repository permissions.

## Learning Objectives

- Understand Open-Source Intelligence (OSINT).
- Learn to retrieve public data through a REST API.
- Process JSON responses in Python.
- Organize collected information into structured reports.
- Identify potential digital exposure.
- Apply defensive security practices.

## Limitations

- Only information returned by GitHub's public API is collected.
- The tool retrieves at most 10 recent public repositories.
- Programming-language counts represent only the retrieved repositories.
- Public profile information does not reliably reveal private habits, colleagues, or personal routines.
- The assessment uses basic checks and does not constitute a comprehensive security audit.
- API rate limits and network failures may affect results.

## Ethical Use

Use this tool for educational purposes and authorized defensive assessments. Do not use collected information to impersonate individuals, conduct targeted phishing, or access accounts without permission.

## Conclusion

This project demonstrates how Python can collect public GitHub information, produce structured JSON output, and identify opportunities to improve digital privacy and security.
