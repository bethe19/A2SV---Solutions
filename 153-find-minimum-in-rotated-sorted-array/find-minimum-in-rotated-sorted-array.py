class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]