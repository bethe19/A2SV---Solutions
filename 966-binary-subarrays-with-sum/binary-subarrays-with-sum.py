class Solution:
    def numSubarraysWithSum(self, nums, goal):
        freq = defaultdict(int)
        freq[0] = 1  # empty prefix
        
        curr = 0
        ans = 0
        
        for x in nums:
            curr += x
            need = curr - goal
            ans += freq.get(need, 0)
            freq[curr] += 1
        
        return ans
