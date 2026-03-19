class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()
        l = 0
        ans = 0

        for r, x in enumerate(nums):
            while max_dq and max_dq[-1] < x:
                max_dq.pop()
            max_dq.append(x)
            while min_dq and min_dq[-1] > x:
                min_dq.pop()
            min_dq.append(x)
            while max_dq[0] - min_dq[0] > limit:
                if nums[l] == max_dq[0]:
                    max_dq.popleft()
                if nums[l] == min_dq[0]:
                    min_dq.popleft()
                l += 1

            ans = max(ans, r - l + 1)

        return ans
