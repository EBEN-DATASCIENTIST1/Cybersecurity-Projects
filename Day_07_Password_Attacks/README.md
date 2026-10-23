# Day 7 — Password Attacks and Rate Limiting

## Overview

This project demonstrates password-guessing behavior in a controlled local environment and shows how a Flask login server can temporarily block repeated failed login attempts.

## Objectives

- Understand brute-force password attacks.
- Simulate a small number of password guesses against a local test server.
- Implement a basic rate limiter.
- Interpret HTTP 200, 401, and 429 responses.
- Generate a JSON report and defensive analysis.

## Technologies

- Python
- Flask
- Requests
- PowerShell

## Features

- Local Flask login endpoint.
- Fictional test account.
- Five-failure threshold and 30-second temporary block.
- Bounded password test list.
- Request timeout and basic error handling.
- JSON report without password values.
- Defensive analysis and lab journal.

## Installation

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Start the local server:

```bash
python -m src.lab_server
```

Keep the server running. Open a second terminal and run:

```bash
python -m src.brute_force_simulator
```

The simulator sends requests only to `127.0.0.1:5000`.

## Generated Reports

- `reports/simulation_report.json` — simulation outcomes.
- `reports/defensive_analysis.txt` — attacker and defender perspectives.
- `reports/lab_journal.txt` — experiment scope, activities, and results.

## Results

The simulator demonstrated rejected login attempts and successful authentication using the fictional lab account. A separate test confirmed that repeated failures triggered HTTP 429 responses.

## Limitations

This is an educational demonstration, not production-ready authentication. Its in-memory rate limiter resets when the server restarts and does not provide persistent or distributed protection. The project does not implement production-grade password storage or multi-factor authentication.

## Ethical Scope

Testing is restricted to the local lab server and fictional credentials. Do not use this simulator against real accounts or systems without explicit authorization.
