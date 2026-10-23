
import json
from pathlib import Path


def fake_profile_score(profile):
    """Calculate a heuristic risk score from 0 to 100."""
    score = 0

    age_days = profile.get("account_age_days", 365)
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    posts = profile.get("posts", 100)

    if age_days < 30:
        score += 30

    if following / max(followers, 1) > 10:
        score += 25

    if profile.get("no_profile_pic", False):
        score += 20

    if posts < 5:
        score += 15

    if profile.get("default_bio", False):
        score += 10

    return min(score, 100)


def get_risk_level(score):
    """Return a risk category for the heuristic score."""
    if score >= 70:
        return "HIGH"
    if score >= 40:
        return "MEDIUM"
    return "LOW"


def main():
    input_file = Path("data/sample_profiles.json")
    output_file = Path("reports/profile_analysis.json")

    try:
        profiles = json.loads(input_file.read_text(encoding="utf-8"))
        if not isinstance(profiles, list):
            raise ValueError("Input must contain a JSON list.")

        results = []

        for profile in profiles:
            if not isinstance(profile, dict):
                raise ValueError("Each profile must be a JSON object.")

            score = fake_profile_score(profile)
            label = str(profile.get("label", "Unknown"))

            result = {
                "label": label,
                "score": score,
                "risk_level": get_risk_level(score),
                "warning": "Heuristic result, not proof of impersonation.",
            }
            results.append(result)

            print(
                f"{label}: score={score}/100, "
                f"risk={result['risk_level']}"
            )

        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            json.dumps(results, indent=2),
            encoding="utf-8",
        )
        print(f"\nReport saved to: {output_file}")

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Could not analyze profiles: {error}")


if __name__ == "__main__":
    main()
