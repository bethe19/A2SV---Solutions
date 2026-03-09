class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        total = rows * cols
        res = [[rStart, cStart]]
        if total == 1:
            return res

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        step = 1

        while len(res) < total:
            for d in range(4):
                dr, dc = dirs[d]
                moves = step
                if d == 2 or d == 3:
                    moves = step + (0 if d == 2 else 0)

                for _ in range(moves):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                if d % 2 == 1:
                    step += 1

        return res
