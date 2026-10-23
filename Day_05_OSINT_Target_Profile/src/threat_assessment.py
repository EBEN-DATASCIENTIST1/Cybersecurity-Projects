
def assess_profile(profile):
    findings = []

    if profile.get("bio"):
        findings.append(
            "Public bio is available. Review it for information "
            "that should not be disclosed."
        )

    if profile.get("company"):
        findings.append(
            "Company information is public. Check that its "
            "disclosure is intentional."
        )

    if profile.get("location"):
        findings.append(
            "Location information is public. Consider whether "
            "this level of detail is necessary."
        )

    repos = profile.get("recent_public_repositories", [])

    if repos:
        findings.append(
            f"{len(repos)} recent public repositories were listed. "
            "Review them for accidentally committed secrets."
        )

    if not findings:
        findings.append(
            "No profile exposure indicators were identified "
            "by these basic checks."
        )

    return findings


def create_threat_report(profile, findings):
    username = profile.get("username") or "Unknown"

    lines = [
        "GITHUB PUBLIC EXPOSURE ASSESSMENT",
        "=" * 40,
        f"Profile: {username}",
        "",
        "Findings:"
    ]

    lines.extend(f"- {finding}" for finding in findings)

    lines.extend([
        "",
        "Recommended defensive actions:",
        "- Review public profile fields and remove unnecessary details.",
        "- Inspect repositories for accidentally exposed credentials.",
        "- Revoke and rotate any exposed secrets immediately.",
        "- Enable two-factor authentication.",
        "- Review repository visibility and access permissions.",
        "",
        "Limitations:",
        "This is a basic exposure review, not a verified security audit."
    ])

    return "\n".join(lines)
