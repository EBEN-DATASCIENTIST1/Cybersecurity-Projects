# Day 9 — Fake Profile Detection

## Overview

This project uses Python to calculate heuristic risk scores for fictional social media profiles. It demonstrates how selected profile characteristics can help identify accounts that may warrant further review.

## Objectives

- Understand social media impersonation risks.
- Apply simple behavioral heuristics.
- Calculate profile risk scores.
- Generate a JSON analysis report.
- Learn the limitations of automated profile classification.

## Technologies

- Python
- JSON
- Python standard library

## Features

- Scores account age, follower-to-following ratio, profile-picture availability, post count, and biography characteristics.
- Assigns LOW, MEDIUM, or HIGH risk categories.
- Analyzes multiple fictional profiles.
- Saves results as JSON.
- Handles file and JSON parsing errors.

## Usage

Run from the project root:

```bash
python -m src.fake_profile_detector
```

Input file:

`data/sample_profiles.json`

Output file:

`reports/profile_analysis.json`

## Results

The detector analyzed five fictional profiles and generated scores of 100, 0, 80, 20, and 25.

These results demonstrate the scoring logic; they do not establish whether any real account is authentic or fraudulent.

## Limitations

The scoring rules are educational heuristics and have not been validated against real-world labeled data. False positives and false negatives are possible.

## Ethical Scope

This project uses fictional data only. It does not scrape platforms, contact account owners, or make automated accusations against real people. Anonymize any future authorized data before sharing it.
