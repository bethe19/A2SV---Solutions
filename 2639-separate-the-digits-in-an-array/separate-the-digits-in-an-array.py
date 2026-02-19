class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num = ''
        for i in nums:
            num += str(i)
        num = list(num)
        num = [int(i) for i in num]
        return num