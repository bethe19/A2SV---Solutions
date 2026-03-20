# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, p, q, s):
        if q is None and p is None:
            return
        elif q is None or p is None or q.val != p.val:
            s[0] = False
        if s[0] is False:
            return
        self.inorder(q.left, p.left, s)
        self.inorder(q.right, p.right, s)

    def isSameTree(self, p, q):
        s = [True]
        self.inorder(p, q, s)
        return s[0]
