
from pathlib import Path
import requests

from src.email_harvester import (
    harvest_from_file,
    harvest_from_url
)


def save_report(emails):
    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    report_file = report_dir / "found_emails.txt"

    content = "\n".join(sorted(emails))
    report_file.write_text(content + ("\n" if content else ""), encoding="utf-8")

    print(f"\nReport saved to: {report_file}")


def main():
    print("=" * 45)
    print("       EMAIL HARVESTER LAB")
    print("=" * 45)
    print("1. Test local HTML file")
    print("2. Scan an authorized webpage")

    choice = input("Choose an option (1 or 2): ").strip()

    try:
        if choice == "1":
            sample_file = Path("data") / "sample.html"
            emails = harvest_from_file(sample_file)

        elif choice == "2":
            url = input("Enter authorized webpage URL: ").strip()

            if not url.startswith(("https://", "http://")):
                print("Please enter a valid HTTP or HTTPS URL.")
                return

            emails = harvest_from_url(url)

        else:
            print("Invalid option. Choose 1 or 2.")
            return

        print("\nEmail addresses found:")

        if emails:
            for email in sorted(emails):
                print(email)
        else:
            print("No email addresses found.")

        save_report(emails)

    except (OSError, requests.RequestException) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
