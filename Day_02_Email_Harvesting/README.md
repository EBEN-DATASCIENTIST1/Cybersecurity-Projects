# Day 2 — Email Harvesting & Social Engineering Prep

## Overview

This project is a Python-based email harvesting tool developed for cybersecurity education. It extracts email addresses from HTML content and authorized webpages.

The project demonstrates how publicly exposed email addresses can be discovered and why organizations should understand their exposure to social engineering risks.

## Features

- Extract email addresses using regular expressions.
- Remove duplicate email addresses.
- Read email addresses from a local HTML test file.
- Retrieve HTML from an authorized webpage using HTTP requests.
- Handle invalid URLs and network errors.
- Save extracted addresses to a text report.

## Technologies Used

- Python
- Requests
- Regular expressions (`re`)
- pathlib

## Project Structure

```text
Day_02_Email_Harvesting/
├── data/
│   └── sample.html
├── reports/
│   └── found_emails.txt
├── screenshots/
├── src/
│   └── email_harvester.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Open a terminal in the project directory and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Choose one of the available options:

1. Test the local HTML sample.
2. Scan an authorized webpage.

For webpage testing, enter a complete HTTP or HTTPS URL.

The program extracts email addresses visible in the returned HTML and saves the results to `reports/found_emails.txt`.

## Limitations

- Only addresses matching the configured regular expression are extracted.
- Addresses loaded dynamically by JavaScript may not appear in the retrieved HTML.
- Some websites may block automated requests or limit access.
- A successful request does not guarantee that an email address will be found.
- The current report file is overwritten each time a scan is completed.

## Ethical Use

Use this tool only on webpages you own or have permission to assess. Do not use harvested contact information for spam, phishing, impersonation, or other unauthorized activities.

## Learning Objectives

- Understand email harvesting and its relationship to social engineering.
- Learn regular-expression-based text extraction.
- Make HTTP requests with Python.
- Handle network errors.
- Generate simple text reports.
- Understand the risks of publicly exposed contact information.
