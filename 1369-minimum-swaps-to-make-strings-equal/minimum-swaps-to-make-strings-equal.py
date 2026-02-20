class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        
        for a, b in zip(s1, s2):
            if a == b:
                continue
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        
        if (xy + yx) % 2 == 1:
            return -1
        
        return xy // 2 + yx // 2 + 2 * (xy % 2)
