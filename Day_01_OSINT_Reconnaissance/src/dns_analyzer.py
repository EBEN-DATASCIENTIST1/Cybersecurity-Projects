
import dns.resolver


def analyze_dns(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(
                domain,
                record_type,
                lifetime=5
            )
            results[record_type] = [str(answer) for answer in answers]

        except dns.resolver.NXDOMAIN:
            results[record_type] = []
            break

        except dns.exception.DNSException:
            results[record_type] = []

    return results
