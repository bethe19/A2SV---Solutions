class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        n = len(names)
        for i in range(n):
            map[heights[i]] = names[i]
        
        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    swapped = True
            
            if not swapped:
                break
        names = []
        for i in heights:
            names.append(map[i])
        return names