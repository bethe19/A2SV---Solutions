class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        list_nums = sorted(map, key=map.get, reverse=True)
        return list_nums[0:k]