
import json
from datetime import datetime, timezone
from pathlib import Path

REPORT_DIR = Path("reports")

SEVERITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

RESPONSE_ACTIONS = {
    "phishing": [
        "Preserve the original email and relevant mail logs",
        "Report the message to the security team",
        "Review links and attachments in a safe analysis environment",
        "Consider quarantining the message through approved procedures",
    ],
    "credential_compromise": [
        "Contact the identity or security team",
        "Reset affected credentials through the official process",
        "Revoke active sessions where authorized",
        "Review authentication logs for suspicious activity",
    ],
    "suspicious_email_rule": [
        "Review the rule with the account owner",
        "Preserve relevant mailbox audit logs",
        "Remove unauthorized rules through approved procedures",
        "Review mailbox access for suspicious activity",
    ],
    "usb_incident": [
        "Stop using the suspicious USB device",
        "Notify the security team",
        "Follow approved endpoint isolation procedures if needed",
        "Preserve relevant evidence",
    ],
}


def respond_to_incident(incident):
    """Generate a simulated response plan for a security incident."""
    incident_type = incident.get("type", "")
    severity = incident.get("severity", "")
    incident_id = incident.get("incident_id", "SIM-001")

    if incident_type not in RESPONSE_ACTIONS:
        raise ValueError("Unsupported incident type.")

    if severity not in SEVERITIES:
        raise ValueError("Severity must be LOW, MEDIUM, HIGH, or CRITICAL.")

    actions = []

    if severity in {"HIGH", "CRITICAL"}:
        actions.append("Escalate to the security incident response team")

    actions.extend(RESPONSE_ACTIONS[incident_type])

    return {
        "incident_id": incident_id,
        "incident": {
            "type": incident_type,
            "severity": severity,
            "user": incident.get("user", "not provided"),
        },
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "SIMULATION_ONLY",
        "actions": actions,
        "warning": (
            "These are recommendations only. No accounts, sessions, "
            "emails, or devices were changed."
        ),
    }


def main():
    # Fictional incident for local testing.
    incident = {
        "incident_id": "SIM-014",
        "type": "phishing",
        "severity": "HIGH",
        "user": "training-user@example.test",
    }

    try:
        report = respond_to_incident(incident)
    except ValueError as error:
        print(f"Invalid incident: {error}")
        return

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_file = REPORT_DIR / "incident_report.json"

    try:
        report_file.write_text(
            json.dumps(report, indent=2),
            encoding="utf-8",
        )
    except OSError as error:
        print(f"Could not save incident report: {error}")
        return

    print("SIMULATED INCIDENT RESPONSE")
    print("-" * 35)
    print(f"Incident ID: {report['incident_id']}")
    print(f"Type: {report['incident']['type']}")
    print(f"Severity: {report['incident']['severity']}")
    print("\nRecommended actions:")

    for action in report["actions"]:
        print(f"- {action}")

    print(f"\nReport saved to: {report_file}")
    print(report["warning"])


if __name__ == "__main__":
    main()
