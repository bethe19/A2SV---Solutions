class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        cur = []

        def backtrack(start):
            res.append(cur[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                backtrack(i + 1)
                cur.pop()

        backtrack(0)
        return res