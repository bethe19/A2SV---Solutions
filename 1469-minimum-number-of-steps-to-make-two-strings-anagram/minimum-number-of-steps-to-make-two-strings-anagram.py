class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ct = Counter(t)
        
        steps = 0
        for ch in cs:
            if cs[ch] > ct[ch]:
                steps += cs[ch] - ct[ch]
        return steps