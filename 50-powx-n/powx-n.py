class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        neg = n < 0
        n = abs(n)

        result = 1.0
        cur = x
        while n > 0:
            if n & 1:
                result *= cur
            cur *= cur
            n >>= 1

        return 1 / result if neg else result
