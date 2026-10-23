
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


DATA_FILE = Path("data/emails.csv")
REPORT_DIR = Path("reports")


def main():
    try:
        data = pd.read_csv(DATA_FILE)
    except (OSError, pd.errors.ParserError) as error:
        print(f"Could not read dataset: {error}")
        return

    required_columns = {"email_text", "label"}
    if not required_columns.issubset(data.columns):
        print("Dataset must contain email_text and label columns.")
        return

    data = data.dropna(subset=["email_text", "label"])
    data["email_text"] = data["email_text"].astype(str)
    data["label"] = pd.to_numeric(data["label"], errors="coerce")
    data = data.dropna(subset=["label"])

    if not set(data["label"].unique()).issubset({0, 1}):
        print("Labels must be 0 (legitimate) or 1 (phishing).")
        return

    if data["label"].nunique() != 2 or data["label"].value_counts().min() < 2:
        print("Dataset needs at least two examples per class.")
        return

    X_train, X_test, y_train, y_test = train_test_split(
        data["email_text"],
        data["label"].astype(int),
        test_size=0.30,
        random_state=42,
        stratify=data["label"].astype(int),
    )

    model = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB()),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions, labels=[0, 1])
    details = classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["Legitimate", "Phishing"],
        zero_division=0,
    )

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    report = (
        "DAY 12 — PHISHING EMAIL CLASSIFIER\n\n"
        f"Dataset size: {len(data)}\n"
        f"Training samples: {len(X_train)}\n"
        f"Testing samples: {len(X_test)}\n"
        f"Accuracy: {accuracy:.2%}\n\n"
        "Confusion matrix (actual rows, predicted columns):\n"
        f"{matrix}\n\n"
        "Classification report:\n"
        f"{details}\n"
        "Note: This small fictional dataset is for learning only.\n"
    )

    (REPORT_DIR / "model_report.txt").write_text(
        report,
        encoding="utf-8",
    )

    print(report)
    print("Report saved to reports/model_report.txt")


if __name__ == "__main__":
    main()
