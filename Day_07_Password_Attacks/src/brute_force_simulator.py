
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

URL = "http://127.0.0.1:5000/login"
USERNAME = "lab_user"

# Small, fictional test list for the local lab only.
TEST_PASSWORDS = [
    "welcome123",
    "password123",
    "summer2026",
    "LabPass123!",
    "qwerty123",
]

def main():
    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    results = []

    print("LOCAL PASSWORD SECURITY SIMULATOR")
    print("-" * 35)

    for number, password in enumerate(TEST_PASSWORDS, start=1):
        try:
            response = requests.post(
                URL,
                json={
                    "username": USERNAME,
                    "password": password,
                },
                timeout=3,
            )

            status = response.status_code

            if status == 200:
                outcome = "Lab login accepted"
            elif status == 401:
                outcome = "Rejected"
            elif status == 429:
                outcome = "Rate limited"
            else:
                outcome = "Unexpected response"

            print(f"Attempt {number}: HTTP {status} - {outcome}")

            # Do not include password values in the report.
            results.append({
                "attempt": number,
                "http_status": status,
                "outcome": outcome,
            })

            if status == 429:
                print("Stopping because the rate limiter blocked requests.")
                break

            if status == 200:
                print("Stopping after the lab accepted a password.")
                break

        except requests.RequestException as error:
            print(f"Request failed: {type(error).__name__}")
            results.append({
                "attempt": number,
                "outcome": "Request failed",
                "error_type": type(error).__name__,
            })
            break

    report = {
        "project": "Day 7 - Password Security Lab",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Localhost only",
        "attempts": results,
    }

    report_file = report_dir / "simulation_report.json"
    try:
        report_file.write_text(
            json.dumps(report, indent=2),
            encoding="utf-8",
        )
        print(f"\nReport saved to: {report_file}")
    except OSError as error:
        print(f"Could not save report: {error}")

if __name__ == "__main__":
    main()
