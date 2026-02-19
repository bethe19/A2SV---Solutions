class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for x in nums:
            if x % 2 == 0:
                even_sum += x

        ans = []
        for val, idx in queries:
            old = nums[idx]
            new = old + val
            nums[idx] = new

            if old % 2 == 0:
                even_sum -= old
            if new % 2 == 0:
                even_sum += new

            ans.append(even_sum)
        return ans
