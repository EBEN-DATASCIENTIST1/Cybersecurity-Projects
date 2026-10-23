# Day 13 — SIEM Log Analysis for Social Engineering Detection

## Overview

This project uses Python to parse fictional security logs and flag repeated failed logins and email-rule creation events.

## Objectives

- Understand SIEM log analysis.
- Parse structured security events.
- Detect repeated authentication failures.
- Flag email-rule changes for investigation.
- Generate a JSON alert report.

## Technologies

- Python
- Regular expressions
- `collections.Counter`
- JSON
- `datetime` and `pathlib`

All dependencies are included with Python.

## Features

- Parses login and email-rule events.
- Validates timestamps.
- Identifies malformed log entries.
- Counts failed logins by user and IP address.
- Flags email-rule creation.
- Saves alerts to JSON.

## Usage

Run from the project root:

```bash id="i7ym3g"
python -m src.log_analyzer
```

Input file:

`data/sample_logs.txt`

Output file:

`reports/siem_alerts.json`

## Results

The sample dataset contained eight parsed events and produced four alerts.

- Four failed logins.
- Two successful logins.
- Two email-rule creation events.

## Limitations

This is an educational parser using fictional data. Its alerts require human investigation and do not prove that an attack occurred.

## Ethical Scope

Only local sample logs are analyzed. No live accounts, mailboxes, or external systems are accessed.
