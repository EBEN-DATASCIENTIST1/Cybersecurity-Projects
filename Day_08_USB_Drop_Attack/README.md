# Day 8 — USB Drop Attack Simulation

## Overview

This project demonstrates a benign USB drop attack awareness scenario using Python. It records basic system information when manually executed and saves the results to a local JSON report.

## Objectives

- Understand USB drop attacks.
- Demonstrate basic system-information collection.
- Learn about USB security and prevention.
- Generate a structured JSON report.

## Technologies

- Python
- Standard Python libraries: `json`, `platform`, `socket`, `datetime`, `getpass`, and `pathlib`

## Features

- Records the execution timestamp in UTC.
- Records hostname, operating system, OS version, username, and working directory.
- Saves results in JSON format.
- Handles file-writing errors.
- Uses no external packages.
- Does not perform network communication or automatic execution.

## Usage

From the project root, run:

```bash
python -m src.usb_payload_simulator
```

The report is saved to:

`reports/recon_log.json`

## Reports

- `reports/recon_log.json` — simulated system-information report.
- `reports/defensive_analysis.txt` — attack perspective, defensive measures, and limitations.
- `reports/lab_journal.txt` — experiment scope, activities, and results.

## Defensive Recommendations

Avoid unknown USB devices, disable unnecessary AutoRun behavior, enforce device-control policies, maintain endpoint protection, and educate users about USB-based threats.

## Limitations

This is an educational simulation, not a full USB attack emulator or a production security tool. It runs manually and does not configure automatic execution.

## Ethical Scope

The simulation is intended for the developer's own computer or an explicitly authorized lab. Anonymize local identifying information before sharing reports publicly.
