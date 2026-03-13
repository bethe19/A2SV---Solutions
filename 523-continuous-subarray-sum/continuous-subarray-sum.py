class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_to_index = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            running_sum %= k

            if running_sum not in remainder_to_index:
                remainder_to_index[running_sum] = i
            else:
                if i - remainder_to_index[running_sum] >= 2:
                    return True

        return False
