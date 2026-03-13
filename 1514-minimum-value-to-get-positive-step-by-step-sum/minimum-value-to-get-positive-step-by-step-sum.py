class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_pref = 0
        for x in nums:
            prefix += x
            if prefix < min_pref:
                min_pref = prefix
        return 1 - min_pref
