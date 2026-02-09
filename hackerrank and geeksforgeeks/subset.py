#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a = Counter(a)
        b = Counter(b)
        for i,j in b.items():
            if a[i] < j :
                return False
                
        return True