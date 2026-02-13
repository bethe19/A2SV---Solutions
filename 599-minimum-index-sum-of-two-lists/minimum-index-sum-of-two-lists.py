class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {}
        minimumSum = 2000
        res = []
        for index, item in enumerate(list1):
            map1[item] = index
        for index, item in enumerate(list2):
            if item in map1:
                sum = map1[item] + index
                if minimumSum == sum:
                    res.append(item)
                elif minimumSum > sum:
                    minimumSum = sum
                    res = [item]
                else:
                    continue
        return res
                    

        