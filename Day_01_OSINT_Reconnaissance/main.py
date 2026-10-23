
from src.osint_scanner import osint_scan, is_valid_domain


def main():
    print("=" * 45)
    print("       OSINT RECONNAISSANCE TOOL")
    print("=" * 45)

    domain = input("Enter a domain to investigate: ").strip()

    if not is_valid_domain(domain):
        print("Invalid domain format. Please try again.")
        return

    osint_scan(domain.rstrip("."))


if __name__ == "__main__":
    main()
