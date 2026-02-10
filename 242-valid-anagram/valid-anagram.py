class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        counter_s = Counter(s)
        counter_t = Counter(t)
        for i,j in counter_s.items():
            if i not in counter_t or j != counter_t[i]:
                return False
        
        return True