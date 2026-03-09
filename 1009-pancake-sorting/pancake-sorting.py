class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)

        for cur in range(n, 1, -1):
            idx = arr.index(cur)

            if idx == cur - 1:
                continue

            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])
            res.append(cur)
            arr[:cur] = reversed(arr[:cur])

        return res
