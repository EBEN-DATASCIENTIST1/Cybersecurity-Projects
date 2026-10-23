
from pathlib import Path
from src.phishing_detector import phish_score



def get_risk_level(score):
    if score >= 70:
        return "CRITICAL"
    elif score >= 40:
        return "HIGH"
    elif score >= 20:
        return "MEDIUM"
    return "LOW"


def main():
    print("=" * 45)
    print("       PHISHING URL DETECTOR")
    print("=" * 45)
    print("1. Analyze one URL")
    print("2. Analyze all sample URLs")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        urls = [input("Enter a URL to analyze: ").strip()]
    elif choice == "2":
        file_path = Path("data") / "sample_urls.txt"

        try:
            urls = [
                line.strip()
                for line in file_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
        except OSError as error:
            print(f"Could not read sample URLs: {error}")
            return
    else:
        print("Invalid option.")
        return

    results = []

    for url in urls:
        score, reasons = phish_score(url)
        risk = get_risk_level(score)

        result = (
            f"URL: {url}\n"
            f"Score: {score}/100\n"
            f"Risk: {risk}\n"
            f"Indicators: {'; '.join(reasons)}\n"
        )

        results.append(result)
        print("\n" + result)

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)
    report_file = report_dir / "phishing_report.txt"

    report_file.write_text(
        "\n".join(results),
        encoding="utf-8"
    )

    print(f"\nReport saved to: {report_file}")


if __name__ == "__main__":
    main()
