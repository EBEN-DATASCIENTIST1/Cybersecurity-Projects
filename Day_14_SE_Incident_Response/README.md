# Day 14 — Social Engineering Incident Response Plan

## Overview

This project generates a structured incident-response plan for simulated social engineering incidents using Python.

## Objectives

- Understand the incident response lifecycle.
- Generate recommended containment and recovery actions.
- Validate incident types and severity.
- Save incident details as JSON.

## Technologies

- Python
- JSON
- `datetime`
- `pathlib`

All dependencies are included with Python.

## Features

- Supports phishing, credential compromise, suspicious email rules, and USB incidents.
- Validates incident type and severity.
- Recommends escalation for HIGH and CRITICAL incidents.
- Generates UTC timestamps.
- Saves a structured JSON report.
- Performs no real containment actions.

## Usage

Run from the project root:

```bash
python -m src.incident_response
```

The output is saved to:

`reports/incident_report.json`

## Deliverables

- `reports/incident_report.json` — simulated incident report.
- `reports/incident_response_playbook.txt` — incident response lifecycle.
- `reports/defensive_analysis.txt` — implementation and limitations.
- `reports/lab_journal.txt` — scope, activities, and results.

## Limitations

This is an educational simulation. It does not integrate with live security tools or execute account, email, or device changes.

## Ethical Scope

Only fictional incident data is used. Real incident response must follow approved organizational procedures and authorization requirements.
