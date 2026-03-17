class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            rem = prefix % k

            ans += count[rem]
            count[rem] += 1

        return ans