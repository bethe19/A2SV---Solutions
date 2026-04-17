"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        visited = set()
        arr = {}

        def traverse(curr):
            if curr in visited:
                return
            visited.add(curr)
            arr[curr] = Node(curr.val)
            
            for i in curr.neighbors:
                traverse(i)
                arr[curr].neighbors.append(arr[i])

        traverse(node)
        return arr[node]