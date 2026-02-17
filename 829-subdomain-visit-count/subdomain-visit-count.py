class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for entry in cpdomains:
            cnt_str, domain = entry.split()
            cnt = int(cnt_str)

            parts = domain.split('.')
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counts[sub] += cnt
        return [f"{c} {d}" for d, c in counts.items()]
