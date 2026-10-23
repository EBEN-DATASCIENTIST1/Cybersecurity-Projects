# Day 15 — Social Engineering Attack Chain Simulator

## Overview

A Python command-line training tool that combines five cybersecurity demonstrations: passive DNS resolution, fictional profile analysis, phishing URL scoring, awareness guidance, and simulated incident response.

## Objectives

- Integrate multiple security concepts into one application.
- Practice input validation and report generation.
- Understand social engineering detection and response.
- Demonstrate ethical cybersecurity testing.

## Technologies

- Python
- `socket`
- `json`
- `datetime`
- `pathlib`

The core application uses Python's standard library.

## Features

- Passive DNS resolution for a supplied domain.
- Heuristic analysis of fictional profile attributes.
- Basic phishing URL scoring.
- Scenario-based awareness guidance.
- Simulated incident-response recommendations.
- JSON report generation.

## Usage

From the project root, run:

```bash id="f7qf1k"
python -m src.chain_simulator
```

Select a module from the menu and follow the prompts. Select `6` to exit.

## Reports

The application creates the following files in `reports`:

- `chain_osint.json`
- `chain_profile_review.json`
- `chain_phishing_score.json`
- `chain_awareness.json`
- `chain_incident_response.json`

## Limitations

The modules are demonstrations, not a production security platform. DNS resolution is limited to address lookup; profile data is fictional; URL scoring uses simple heuristics; and incident response only produces recommendations.

## Ethical Scope

Only assess domains you are authorized to assess. The tool does not send phishing emails, collect credentials, exploit systems, or execute real containment actions. Treat automated scores as indicators that may require further investigation.
