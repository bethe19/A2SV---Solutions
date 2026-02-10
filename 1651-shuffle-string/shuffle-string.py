class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        s = ("").join(res)
        return s
