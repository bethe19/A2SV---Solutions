class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate90(a: List[List[int]]) -> List[List[int]]:
            return [[a[n - 1 - j][i] for j in range(n)] for i in range(n)]

        cur = mat
        for _ in range(4):
            if cur == target:
                return True
            cur = rotate90(cur)

        return False
