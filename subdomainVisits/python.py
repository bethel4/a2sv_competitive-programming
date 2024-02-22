class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)

            subdomains = domain.split(".")
            current_domain = ""
            
            for subdomain in reversed(subdomains):
                current_domain = subdomain + ("" if current_domain == "" else "." + current_domain)
                domain_counts[current_domain] = domain_counts.get(current_domain, 0) + count

        result = [f"{count} {domain}" for domain, count in domain_counts.items()]
        return result
