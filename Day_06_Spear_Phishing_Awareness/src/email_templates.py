
def generate_email(target, scenario):
    """Generate a fictional phishing-awareness training example."""

    templates = {
        "IT Support": {
            "subject": "Training Example: Unexpected IT Account Alert",
            "scenario": (
                "A message claims to come from IT support and reports "
                "unusual account activity."
            ),
            "warning_signs": [
                "Unexpected account warnings",
                "Pressure to act immediately",
                "Requests for passwords or authentication codes",
            ],
            "safe_action": (
                "Contact IT through the organization's official helpdesk."
            ),
            "technique": "Authority and fear of losing account access",
        },
        "Banking": {
            "subject": "Training Example: Suspicious Banking Message",
            "scenario": (
                "A message claims that a bank account requires "
                "urgent verification."
            ),
            "warning_signs": [
                "Urgent requests involving money",
                "Unfamiliar links or attachments",
                "Requests for banking credentials or codes",
            ],
            "safe_action": (
                "Use the official banking app or verified bank contact details."
            ),
            "technique": "Urgency and fear of financial loss",
        },
        "Government": {
            "subject": "Training Example: Suspicious Official Notice",
            "scenario": (
                "A message claims that an official document requires "
                "immediate attention."
            ),
            "warning_signs": [
                "Threats of penalties",
                "Pressure to make immediate payments",
                "Requests for sensitive personal information",
            ],
            "safe_action": (
                "Verify the notice through the relevant department's "
                "official website or published contact details."
            ),
            "technique": "Authority and fear of penalties",
        },
    }

    if scenario not in templates:
        raise ValueError(f"Unknown scenario: {scenario}")

    details = templates[scenario]

    warning_list = "\n".join(
        f"- {warning}" for warning in details["warning_signs"]
    )

    return f"""SECURITY AWARENESS TRAINING EXAMPLE
=====================================

To: {target["email"]}
Subject: {details["subject"]}

Hello {target["name"]},

SCENARIO
{details["scenario"]}

PSYCHOLOGICAL TECHNIQUE
{details["technique"]}

WARNING SIGNS
{warning_list}

SAFE RESPONSE
{details["safe_action"]}

DEFENSIVE LESSON
Do not disclose passwords or one-time authentication codes.
Do not act under pressure. Verify unexpected requests using
an independent, official communication channel.

This is a fictional awareness-training example.
Do not send it to real recipients.
"""
