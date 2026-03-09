class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        res = []
        i = j = 0
        up = True
        
        for _ in range(m * n):
            res.append(mat[i][j])
            
            if up:
                ni, nj = i - 1, j + 1
                if 0 <= ni < m and 0 <= nj < n:
                    i, j = ni, nj
                else:
                    if j == n - 1:
                        i += 1
                    else:
                        j += 1
                    up = False
            else:
                ni, nj = i + 1, j - 1
                if 0 <= ni < m and 0 <= nj < n:
                    i, j = ni, nj
                else:
                    if i == m - 1:
                        j += 1
                    else:
                        i += 1
                    up = True
        
        return res
