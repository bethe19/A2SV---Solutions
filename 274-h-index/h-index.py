class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() 
        n = len(citations)
        h = 0
        for i in range(n):
            h_candidate = min(citations[i], n - i)
            h = max(h, h_candidate)
        return h
