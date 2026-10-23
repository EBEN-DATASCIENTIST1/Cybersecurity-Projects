
import json
from datetime import datetime, timezone
from pathlib import Path

from src.email_templates import generate_email


TARGET = {
    "name": "Alex Example",
    "email": "alex@example.test",
}

SCENARIOS = ["IT Support", "Banking", "Government"]


def main():
    """Generate and save the awareness-training reports."""

    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    results = []

    print("=" * 45)
    print(" SPEAR PHISHING AWARENESS TRAINER")
    print("=" * 45)

    for scenario in SCENARIOS:
        try:
            email_text = generate_email(TARGET, scenario)
        except ValueError as error:
            print(f"Skipping scenario: {error}")
            continue

        filename = scenario.lower().replace(" ", "_") + ".txt"
        report_file = report_dir / filename

        try:
            report_file.write_text(email_text, encoding="utf-8")
        except OSError as error:
            print(f"Could not save {filename}: {error}")
            continue

        print(f"\n[{scenario.upper()}]")
        print(email_text)
        print(f"Saved to: {report_file}")

        results.append({
            "scenario": scenario,
            "file": filename,
            "purpose": "Security-awareness training",
            "recipient": TARGET["email"],
        })

    summary = {
        "project": "Day 6 - Spear Phishing Awareness Training",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Fictional local lab only",
        "scenarios": results,
    }

    summary_file = report_dir / "training_summary.json"

    try:
        summary_file.write_text(
            json.dumps(summary, indent=2),
            encoding="utf-8",
        )
        print(f"\nJSON summary saved to: {summary_file}")
    except OSError as error:
        print(f"Could not save JSON summary: {error}")

    print(f"\nGenerated {len(results)} of {len(SCENARIOS)} reports.")


if __name__ == "__main__":
    main()
