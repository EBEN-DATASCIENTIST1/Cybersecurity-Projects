
def generate_script(target_company, scenario, pretext):
    scenarios = {
        "IT Support": {
            "opener": "A caller claims to be from IT support and reports unusual account activity.",
            "trigger": "Authority and fear of losing access to workplace systems.",
            "warning": "The caller asks for a password or authentication code.",
            "response": "Contact IT using the official helpdesk channel."
        },
        "Banking": {
            "opener": "A message claims that a bank account needs urgent verification.",
            "trigger": "Urgency and fear of financial loss.",
            "warning": "The message requests banking credentials or directs you to an unfamiliar link.",
            "response": "Open the official banking app or contact the bank using its verified number."
        },
        "Government": {
            "opener": "A caller claims that an official document requires immediate attention.",
            "trigger": "Authority and fear of penalties.",
            "warning": "The caller demands immediate payment or sensitive personal information.",
            "response": "Contact the relevant government department through its official website or published contact details."
        }
    }

    details = scenarios[scenario]

    return f"""
=== SOCIAL ENGINEERING AWARENESS SCENARIO ===

Organization: {target_company}
Scenario: {scenario}
Pretext: {pretext}

[SIMULATION OPENER]
{details["opener"]}

[PSYCHOLOGICAL TRIGGER]
{details["trigger"]}

[WARNING SIGN]
{details["warning"]}

[SAFE RESPONSE]
{details["response"]}

[TRAINING LESSON]
Pause before acting. Never disclose passwords or
one-time authentication codes. Verify unexpected
requests through an independent official channel.
"""
