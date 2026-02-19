class Solution:
    def findValidPair(self, s: str) -> str:
        sList = list(s)
        counter_s = Counter(sList)
        
        for i in range(len(s) - 1):
            first, second = s[i], s[i + 1]
            if first != second and counter_s[first] == int(first) and counter_s[second] == int(second):
                return first + second
        
        return ""