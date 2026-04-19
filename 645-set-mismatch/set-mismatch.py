class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        total = sum(nums)
        unique_sum = sum(set(nums))
        expected = n * (n + 1) // 2
        
        duplicate = total - unique_sum
        missing = expected - unique_sum
        
        return [duplicate, missing]