class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        
        ans = 0
        idx = 1
        for _ in range(n):
            ans += piles[idx]
            idx += 2
        return ans
