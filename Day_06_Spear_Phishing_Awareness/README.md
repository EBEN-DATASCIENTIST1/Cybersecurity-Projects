# Day 6 — Spear Phishing Awareness Training

## Overview

This project is a Python-based security-awareness tool that generates fictional email examples illustrating common social engineering techniques.

It demonstrates how attackers may exploit authority, urgency, and fear, while teaching recipients how to recognize suspicious messages and respond safely.

The project is designed for local, authorized cybersecurity training. It does not send emails or collect credentials.

## Features

- Generate IT Support, Banking, and Government awareness scenarios.
- Explain psychological manipulation techniques.
- Identify common phishing warning signs.
- Recommend safe responses.
- Save each scenario as a text report.
- Generate a JSON summary of the experiment.
- Document defensive analysis and lab activity.

## Technologies Used

- Python
- JSON
- pathlib
- datetime

No external Python packages are required.

## Usage

Run the program from the project directory:

```bash
python main.py
```

The program generates three text reports and a JSON summary in the `reports` directory.

## Generated Reports

- `it_support.txt` — IT support impersonation warning signs.
- `banking.txt` — suspicious banking message warning signs.
- `government.txt` — suspicious official notice warning signs.
- `training_summary.json` — generation timestamp, lab scope, and scenario information.
- `defensive_analysis.txt` — attacker and defender perspectives, plus SPF, DKIM, and DMARC explanations.
- `lab_journal.txt` — experiment scope, actions, results, and data-handling notes.

## Learning Objectives

- Understand spear phishing and social engineering.
- Recognize authority, urgency, and fear as manipulation techniques.
- Identify suspicious requests for sensitive information.
- Practice independent verification of unexpected requests.
- Understand the defensive purpose and limitations of SPF, DKIM, and DMARC.

## Ethical and Legal Guidelines

- Use fictional identities and authorized lab environments only.
- Do not send the examples to real recipients.
- Do not collect credentials or confidential personal information.
- Anonymize or delete collected OSINT data after analysis.
- Report accidentally discovered real vulnerabilities to the responsible supervisor.
- Maintain a timestamped lab journal and document the experiment scope.
- Follow applicable laws and institutional policies.

## Limitations

The generated scenarios are educational examples, not a phishing detection system. The program does not send messages, inspect real email infrastructure, or verify SPF, DKIM, or DMARC configurations.

Email authentication can reduce certain forms of domain spoofing, but it does not guarantee that a message is trustworthy.

## Conclusion

This project demonstrates how Python can support security-awareness training by illustrating common social engineering techniques and documenting practical defensive responses.
