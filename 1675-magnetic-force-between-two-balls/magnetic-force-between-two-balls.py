class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def can_place(dist: int) -> bool:
            count = 1
            last = position[0]
            for x in position[1:]:
                if x - last >= dist:
                    count += 1
                    last = x
                    if count >= m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans