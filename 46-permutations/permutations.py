class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)
        path = []

        def back():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                back()
                path.pop()
                used[i] = False

        back()
        return res
