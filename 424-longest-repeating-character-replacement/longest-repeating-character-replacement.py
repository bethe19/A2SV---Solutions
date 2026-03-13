class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0
        n = len(s)

        for right, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])
            while (right - left + 1) - max_freq > k:
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1

        return n - left
