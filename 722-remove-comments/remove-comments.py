class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        in_block = False
        line_buf = []

        for line in source:
            i = 0
            n = len(line)
            if not in_block:
                line_buf = []

            while i < n:
                if in_block:
                    if i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 2
                    else:
                        i += 1 
                else:
                    if i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                        break
                    elif i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 2
                    else:
                        line_buf.append(line[i])
                        i += 1
            if not in_block and line_buf:
                ans.append("".join(line_buf))

        return ans
