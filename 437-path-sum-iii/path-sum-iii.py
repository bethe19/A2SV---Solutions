# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (self.helper(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))

    def helper(self, root: Optional[TreeNode], target: int) -> int:
        if not root:
            return 0
        count = 0
        if root.val == target:
            count += 1
        count += self.helper(root.left, target - root.val)
        count += self.helper(root.right, target - root.val)
        return count
