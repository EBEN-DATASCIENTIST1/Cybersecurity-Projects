
import json
from datetime import datetime, timezone
from pathlib import Path

QUESTIONS = [
    {
        "question": "An email asks you to verify your password using a link. What should you do?",
        "options": [
            "A. Click the link immediately",
            "B. Visit the official website or contact IT directly",
            "C. Reply with your password",
        ],
        "answer": "B",
        "explanation": "Verify requests through trusted channels. Never share your password.",
    },
    {
        "question": "You find an unknown USB drive in a parking lot. What should you do?",
        "options": [
            "A. Plug it into your computer",
            "B. Give it to your organization's security team",
            "C. Take it home and test it",
        ],
        "answer": "B",
        "explanation": "Unknown USB devices may contain malicious files. Do not connect them.",
    },
    {
        "question": "Someone calls claiming to be IT and requests your one-time code. What should you do?",
        "options": [
            "A. Share it to prove your identity",
            "B. Ask them to call back later",
            "C. Refuse and verify through the official IT channel",
        ],
        "answer": "C",
        "explanation": "Never disclose authentication codes to someone who contacts you unexpectedly.",
    },
    {
        "question": "A message says your account will be deleted in five minutes unless you click a link. This may be:",
        "options": [
            "A. An urgency tactic",
            "B. Proof the message is genuine",
            "C. A routine security guarantee",
        ],
        "answer": "A",
        "explanation": "Attackers often create urgency to prevent careful verification.",
    },
    {
        "question": "A stranger asks you to open an unexpected attachment. What is safest?",
        "options": [
            "A. Open it to see what it contains",
            "B. Verify the sender and report it if suspicious",
            "C. Forward it to friends",
        ],
        "answer": "B",
        "explanation": "Unexpected attachments may contain malicious content.",
    },
    {
        "question": "A visitor asks you to hold a secure door open behind an employee. What should you do?",
        "options": [
            "A. Let them enter without checking",
            "B. Ignore the access policy",
            "C. Follow visitor procedures and verify authorization",
        ],
        "answer": "C",
        "explanation": "Tailgating attempts bypass physical access controls.",
    },
    {
        "question": "A social media account offers a prize and asks for your password. What should you do?",
        "options": [
            "A. Do not share credentials; report the account",
            "B. Send your password privately",
            "C. Reuse an old password",
        ],
        "answer": "A",
        "explanation": "Legitimate giveaways do not need your account password.",
    },
    {
        "question": "Your manager unexpectedly asks you to buy gift cards and send the codes. What should you do?",
        "options": [
            "A. Act immediately",
            "B. Verify the request using a known, separate contact method",
            "C. Send the codes before asking questions",
        ],
        "answer": "B",
        "explanation": "Verify unusual financial requests through a trusted channel.",
    },
    {
        "question": "A website asks you to install an unknown browser extension to view a document. What is safest?",
        "options": [
            "A. Install it immediately",
            "B. Disable your security software",
            "C. Verify the source and use an approved alternative",
        ],
        "answer": "C",
        "explanation": "Untrusted extensions can access sensitive browser data.",
    },
    {
        "question": "You suspect you entered your password on a phishing site. What should you do first?",
        "options": [
            "A. Report it and change the password through the official site",
            "B. Wait to see whether anything happens",
            "C. Send the password to a colleague",
        ],
        "answer": "A",
        "explanation": "Use the legitimate service to change the password and report the incident promptly.",
    },
]


def run_quiz():
    score = 0
    results = []

    print("=" * 55)
    print("SOCIAL ENGINEERING AWARENESS QUIZ")
    print("=" * 55)
    print("Enter A, B, or C. Press Ctrl+C to stop.\n")

    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {number}/{len(QUESTIONS)}")
        print(question["question"])

        for option in question["options"]:
            print(f"  {option}")

        while True:
            answer = input("Your answer (A/B/C): ").strip().upper()
            if answer in {"A", "B", "C"}:
                break
            print("Invalid choice. Enter A, B, or C.")

        correct = answer == question["answer"]
        if correct:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. Correct answer: {question['answer']}.")

        print(f"Explanation: {question['explanation']}")

        results.append({
            "question_number": number,
            "selected_answer": answer,
            "correct": correct,
        })

    percentage = round(score / len(QUESTIONS) * 100, 2)

    report = {
        "project": "Day 11 - Social Engineering Awareness",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_questions": len(QUESTIONS),
        "score": score,
        "percentage": percentage,
        "results": results,
    }

    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / "quiz_results.json"

    try:
        report_file.write_text(
            json.dumps(report, indent=2),
            encoding="utf-8",
        )
    except OSError as error:
        print(f"Could not save the report: {error}")
        return

    print("\n" + "=" * 55)
    print(f"FINAL SCORE: {score}/{len(QUESTIONS)} ({percentage}%)")
    print(f"Results saved to: {report_file}")
    print("=" * 55)


if __name__ == "__main__":
    run_quiz()
