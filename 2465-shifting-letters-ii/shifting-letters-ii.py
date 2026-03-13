class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                if end + 1 < n:
                    diff[end + 1] -= 1
            else:
                diff[start] -= 1
                if end + 1 < n:
                    diff[end + 1] += 1
        cur = 0
        res = []
        for i, ch in enumerate(s):
            cur += diff[i]
            shift = cur % 26
            base = ord('a')
            new_pos = (ord(ch) - base + shift) % 26
            res.append(chr(base + new_pos))

        return ''.join(res)
