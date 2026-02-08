class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = Counter(nums)
        return [key for key, val in map.items() if val > len(nums)//3 ]