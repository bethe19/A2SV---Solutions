class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        res = []

        for ch in order:
            idx = ord(ch) - ord('a')
            while freq[idx] > 0:
                res.append(ch)
                freq[idx] -= 1

        for i in range(26):
            while freq[i] > 0:
                res.append(chr(i + ord('a')))
                freq[i] -= 1

        return "".join(res)
