
import json
from datetime import datetime, timezone
from pathlib import Path
import socket

REPORT_DIR = Path("reports")

MODULES = {
    "1": "Passive OSINT",
    "2": "Profile Exposure Review",
    "3": "Phishing URL Scoring",
    "4": "Awareness Email Template",
    "5": "Incident Response Simulation",
    "6": "Exit",
}


def save_report(filename, data):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / filename
    data["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    data["simulation"] = True

    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Report saved to: {path}")



def passive_osint():
    domain = input(
        "Enter a domain you own or are authorized to assess: "
    ).strip().lower().rstrip(".")

    # Validate a hostname, not a URL or path.
    if (
        not domain
        or "://" in domain
        or "/" in domain
        or ":" in domain
        or " " in domain
        or "." not in domain
    ):
        print("Invalid domain. Enter a hostname such as example.com.")
        return

    try:
        results = socket.getaddrinfo(
            domain,
            None,
            type=socket.SOCK_STREAM,
        )
        addresses = sorted({result[4][0] for result in results})
    except socket.gaierror as error:
        print(f"DNS lookup failed: {error}")
        return
    except OSError as error:
        print(f"Could not complete DNS lookup: {error}")
        return

    print(f"\nDomain: {domain}")
    print("Resolved addresses:")
    for address in addresses:
        print(f"- {address}")

    save_report("chain_osint.json", {
        "module": "Passive OSINT",
        "domain": domain,
        "scope": "Authorized domain only",
        "dns_addresses": addresses,
        "note": (
            "DNS resolution only. No port scanning, exploitation, "
            "or service enumeration was performed."
        ),
    })



def profile_review():
    print("Using fictional profile data for this demonstration.")

    profile = {
        "username": "training_user",
        "account_age_days": 7,
        "followers": 2,
        "following": 900,
        "no_profile_pic": True,
        "posts": 1,
        "default_bio": True,
    }

    score = 0
    if profile["account_age_days"] < 30:
        score += 30
    if profile["following"] / max(profile["followers"], 1) > 10:
        score += 25
    if profile["no_profile_pic"]:
        score += 20
    if profile["posts"] < 5:
        score += 15
    if profile["default_bio"]:
        score += 10

    save_report("chain_profile_review.json", {
        "module": "Profile Exposure Review",
        "profile": profile,
        "heuristic_score": min(score, 100),
        "warning": "A high score is not proof that a profile is fake.",
    })


def phishing_url_scoring():
    url = input("Enter a URL for offline heuristic scoring: ").strip()

    indicators = []
    lowered = url.lower()

    if not lowered.startswith("https://"):
        indicators.append("URL does not use HTTPS")
    if "@" in url:
        indicators.append("Contains an @ symbol")
    if any(word in lowered for word in (
        "login", "verify", "password", "account", "secure"
    )):
        indicators.append("Contains a sensitive-action keyword")
    if "xn--" in lowered:
        indicators.append("Contains a possible punycode hostname")

    score = min(len(indicators) * 25, 100)

    save_report("chain_phishing_score.json", {
        "module": "Phishing URL Scoring",
        "url": url,
        "score": score,
        "indicators": indicators,
        "warning": (
            "This simple heuristic is not a verdict. "
            "A score of zero does not guarantee safety."
        ),
    })

    print(f"Heuristic score: {score}/100")
    for indicator in indicators:
        print(f"- {indicator}")


def awareness_template():
    scenario = input(
        "Choose a scenario (IT Support, Banking, Government): "
    ).strip().lower()

    templates = {
        "it support": (
            "Subject: Unexpected account alert",
            "Warning: Verify through your official IT helpdesk. "
            "Never share passwords or authentication codes.",
        ),
        "banking": (
            "Subject: Suspicious banking notification",
            "Warning: Open your official banking app or contact "
            "your bank using a verified number.",
        ),
        "government": (
            "Subject: Unexpected official notice",
            "Warning: Verify the notice through the official "
            "department website or contact channel.",
        ),
    }

    if scenario not in templates:
        print("Unknown scenario. Choose IT Support, Banking, or Government.")
        return

    subject, lesson = templates[scenario]

    save_report("chain_awareness.json", {
        "module": "Awareness Email Template",
        "scenario": scenario,
        "fictional": True,
        "subject": subject,
        "defensive_lesson": lesson,
        "delivery": "Not sent",
    })

    print(subject)
    print(lesson)
    print("Fictional awareness example only; no email was sent.")


def incident_response():
    incident = {
        "incident_id": "SIM-015",
        "type": "phishing",
        "severity": "HIGH",
        "user": "training-user@example.test",
    }

    actions = [
        "Escalate to the security incident response team",
        "Preserve the original message and relevant logs",
        "Review links and attachments safely",
        "Consider email quarantine through approved procedures",
        "Monitor the affected account for suspicious activity",
    ]

    save_report("chain_incident_response.json", {
        "module": "Incident Response Simulation",
        "incident": incident,
        "actions": actions,
        "mode": "SIMULATION_ONLY",
        "warning": "No accounts or systems were modified.",
    })

    print("Simulated incident response plan generated.")
    for action in actions:
        print(f"- {action}")


def main():
    actions = {
        "1": passive_osint,
        "2": profile_review,
        "3": phishing_url_scoring,
        "4": awareness_template,
        "5": incident_response,
    }

    while True:
        print("\n" + "=" * 40)
        print(" SOCIAL ENGINEERING CHAIN SIMULATOR")
        print("=" * 40)

        for key, value in MODULES.items():
            print(f"{key}. {value}")

        choice = input("\nSelect a module: ").strip()

        if choice == "6":
            print("Simulator closed.")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Select 1–6.")
            continue

        try:
            action()
        except (OSError, ValueError) as error:
            print(f"Operation failed: {error}")


if __name__ == "__main__":
    main()
