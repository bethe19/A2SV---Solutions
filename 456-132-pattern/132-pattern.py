class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float('-inf')
        stack = []

        for x in reversed(nums):
            if x < third:
                return True
            while stack and stack[-1] < x:
                third = stack.pop()
            stack.append(x)

        return False