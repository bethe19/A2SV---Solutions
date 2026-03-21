class Solution:
    def minOperations(self, nums):
        n = len(nums)
        ops = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ops += 1
        return ops if nums[-1] == 1 and nums[-2] == 1 else -1
