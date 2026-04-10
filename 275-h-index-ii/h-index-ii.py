class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        h_index = 0

        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            h_temp = citations[mid]
            count = n - mid
            if h_temp >= count:
                h_index = count
                right = mid - 1
            else:
                left = mid + 1
        
        return h_index
            

