
from pathlib import Path
from src.awareness_generator import generate_script


def main():
    scenarios = {
        "1": ("IT Support", "A caller claims there is an account problem."),
        "2": ("Banking", "A message claims an account needs verification."),
        "3": ("Government", "A caller claims urgent action is required.")
    }

    print("=" * 45)
    print(" SOCIAL ENGINEERING AWARENESS TRAINER")
    print("=" * 45)
    print("1. IT Support scenario")
    print("2. Banking scenario")
    print("3. Government scenario")

    choice = input("Choose a scenario (1-3): ").strip()

    if choice not in scenarios:
        print("Invalid choice.")
        return

    company, pretext = scenarios[choice]
    script = generate_script(company, scenarios[choice][0], pretext)

    print(script)

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    filenames = {
        "1": "it_support.txt",
        "2": "banking.txt",
        "3": "government.txt"
    }

    report_file = report_dir / filenames[choice]
    report_file.write_text(script, encoding="utf-8")

    print(f"\nTraining script saved to: {report_file}")


if __name__ == "__main__":
    main()
