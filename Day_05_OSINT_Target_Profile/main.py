
import json
from pathlib import Path

import requests

from src.github_profiler import github_profile
from src.threat_assessment import assess_profile, create_threat_report


def main():
    print("=" * 45)
    print("       GITHUB PUBLIC PROFILE ANALYZER")
    print("=" * 45)

    username = input("Enter an authorized GitHub username: ").strip()

    if (
        not username
        or "/" in username
        or " " in username
        or len(username) > 39
    ):
        print("Invalid GitHub username format.")
        return

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    try:
        # 1. Collect public GitHub profile data
        profile = github_profile(username)

        # 2. Generate JSON profile
        profile_json = json.dumps(
            profile,
            indent=2,
            ensure_ascii=False
        )

        profile_file = report_dir / "github_profile.json"
        profile_file.write_text(
            profile_json,
            encoding="utf-8"
        )

        print("\n[PUBLIC GITHUB PROFILE]")
        print(profile_json)
        print(f"\nProfile saved to: {profile_file}")

        # 3. Assess public information exposure
        findings = assess_profile(profile)

        # 4. Generate threat assessment report
        threat_report = create_threat_report(
            profile,
            findings
        )

        threat_file = report_dir / "threat_assessment.txt"
        threat_file.write_text(
            threat_report,
            encoding="utf-8"
        )

        print("\n" + threat_report)
        print(f"\nThreat assessment saved to: {threat_file}")

        print("\nAnalysis completed successfully.")

    except requests.HTTPError as error:
        if error.response is not None and error.response.status_code == 404:
            print("GitHub user not found. Check the username.")
        elif error.response is not None and error.response.status_code == 403:
            print("GitHub API rate limit or access restriction reached.")
        else:
            print(f"GitHub HTTP request failed: {error}")

    except requests.RequestException as error:
        print(f"Network request failed: {error}")

    except (ValueError, KeyError) as error:
        print(f"Could not process GitHub response: {error}")

    except OSError as error:
        print(f"Could not save report: {error}")


if __name__ == "__main__":
    main()
