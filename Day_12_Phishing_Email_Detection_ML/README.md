# Day 12 — Phishing Email Detection with Machine Learning

## Overview

This project uses a scikit-learn Naive Bayes classifier to classify fictional email text as phishing or legitimate.

## Objectives

- Apply natural language processing to email text.
- Train a Naive Bayes classifier.
- Evaluate predictions with accuracy, precision, recall, F1-score, and a confusion matrix.
- Understand the limitations of phishing detection models.

## Technologies

- Python
- pandas
- scikit-learn

## Features

- Labeled CSV dataset.
- CountVectorizer text features.
- Multinomial Naive Bayes classifier.
- Stratified train/test split.
- Classification metrics and confusion matrix.
- Text report saved to disk.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage

From the project root, run:

```bash
python -m src.phishing_classifier
```

Input dataset:

`data/emails.csv`

Output report:

`reports/model_report.txt`

## Results

The model was evaluated on 15 held-out samples from a dataset of 50 fictional emails.

- Accuracy: 93.33%
- Phishing precision: 1.00
- Phishing recall: 0.86
- Phishing F1-score: 0.92

The confusion matrix showed one missed phishing email and no false positives.

## Limitations

The dataset is small and synthetic. These results do not establish real-world detection performance and should not be interpreted as a guarantee of safety.

## Ethical Scope

The project uses fictional data and does not send phishing emails, collect credentials, or target real users.
