class Solution:
    def maxArea(self, n: List[int]) -> int:
        max_area = 0
        index = len(n) - 1
        i = 0

        while i < index:
            right = n[index]
            left = n[i]
            if right > left:
                min_h = left
            else:
                min_h = right

            area = min_h * (index - i)
            if max_area < area:
                max_area = area
            if min_h == left:
                i += 1
            else:
                index -= 1

        return max_area