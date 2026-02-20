class Solution:
    def setZeroes(self, n: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        k=[]
        for i in range (len(n)):
            if 0 in n[i]:
                for j in range(len(n[i])):
                    if n[i][j]==0:
                        k.append((i,j))
        for i in n:
            for a,b in k:
                i[b]=0
                n[a]=[0]*len(n[a])
        