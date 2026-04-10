class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, currentCombinations):
            if len(currentCombinations) == k:
                res.append(currentCombinations.copy())
                return
            for i in range(start, n+1):
                currentCombinations.append(i)
                backtrack(i+1, currentCombinations)
                currentCombinations.pop()
                
        backtrack(1, [])
        return res
            


