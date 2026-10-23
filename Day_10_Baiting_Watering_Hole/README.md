# Day 10 — Baiting and Watering Hole Attack Simulation

## Overview

This project demonstrates a benign local honeypot that records HTTP visits to a simulated bait link. A Python analyzer summarizes the captured events.

## Objectives

- Understand baiting and watering-hole attacks.
- Demonstrate basic honeypot logging.
- Analyze HTTP request metadata.
- Learn defenses against malicious links and downloads.

## Technologies

- Python
- `http.server`
- `json`
- `datetime`
- `pathlib`
- `collections`

All dependencies are included with Python.

## Features

- Local-only HTTP server.
- UTC timestamps for recorded visits.
- Request path and User-Agent logging.
- JSON Lines log format.
- Summary of total visits, unique paths, and User-Agent counts.
- Error handling for log files and malformed JSON records.

## Usage

Start the honeypot:

```bash id="s55p6a"
python -m src.honeypot_server
```

Keep the server running and open a second terminal. Send a local test request:

```powershell id="lq7ht2"
Invoke-WebRequest -Uri "http://127.0.0.1:8080/bait-download" -UseBasicParsing
```

Analyze the captured visits:

```bash id="jty1oa"
python -m src.log_analyzer
```

## Reports

- `reports/visit_log.jsonl` — recorded HTTP visits.
- `reports/visit_analysis.json` — visit summary.
- `reports/defensive_analysis.txt` — attack concepts and mitigation measures.
- `reports/lab_journal.txt` — experiment scope, activities, and results.

## Results

The local test recorded one visit to `/bait-download`. The analyzer produced a JSON summary containing one visit and one unique path.

## Limitations

This is a local educational demonstration. It does not exploit browsers, deliver malware, download files, or identify malicious intent from a visit alone.

## Ethical Scope

Testing is restricted to localhost. Keep raw logs private because they may contain IP addresses and User-Agent information. Anonymize logs and screenshots before public sharing.
