class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = list(set(nums))
        return len(distinct) != len(nums) 