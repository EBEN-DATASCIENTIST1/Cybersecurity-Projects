# Day 11 — Social Engineering Awareness Training

## Overview

This project is an interactive Python command-line quiz designed to teach users how to recognize common social engineering threats and respond safely.

## Objectives

- Recognize common social engineering tactics.
- Practice safer responses to suspicious requests.
- Receive immediate feedback and explanations.
- Track quiz scores in a JSON report.

## Technologies

- Python
- JSON
- Python standard library

## Features

- Ten scenario-based questions.
- Three answer choices per question.
- Input validation.
- Immediate feedback and explanations.
- Score and percentage calculation.
- JSON results report.

## Usage

From the project root, run:

```bash id="m7w7jv"
python -m src.awareness_quiz
```

Answer each question using A, B, or C.

## Reports

- `reports/quiz_results.json` — score, percentage, and per-question results.
- `reports/defensive_analysis.txt` — topics, results, and defensive recommendations.
- `reports/lab_journal.txt` — experiment scope, activities, and results.

## Test Results

The initial test run scored 5/10 (50%). The quiz completed successfully and saved the results report.

## Limitations

This is an educational quiz, not a comprehensive measure of security awareness. Its questions cover selected scenarios only.

## Ethical Scope

All scenarios are fictional. The application does not send phishing messages, collect credentials, or target real users.
