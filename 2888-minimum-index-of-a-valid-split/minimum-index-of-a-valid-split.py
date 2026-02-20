class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        total = sum(1 for x in nums if x == candidate)
        left = 0
        for i, x in enumerate(nums):
            if x == candidate:
                left += 1

            left_len = i + 1
            right_len = n - left_len
            if right_len == 0:
                break

            right = total - left

            if left * 2 > left_len and right * 2 > right_len:
                return i

        return -1
