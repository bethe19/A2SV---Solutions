class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        deltas = []
        for a, b in costs:
            total += a
            deltas.append(b - a)
        
        deltas.sort()
        
        n = len(costs) // 2
        for i in range(n):
            total += deltas[i]
        
        return total