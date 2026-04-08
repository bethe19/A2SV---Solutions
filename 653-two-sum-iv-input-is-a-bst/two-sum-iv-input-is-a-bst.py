# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional['TreeNode'], k: int) -> bool:
        arr = []

        def inorder(node, arr):
            if node is None:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        def twoSum(numbers: List[int], target: int) -> bool:
            left, right = 0, len(numbers) - 1
            while left < right:
                s = numbers[left] + numbers[right]
                if s == target:
                    return True
                elif s > target:
                    right -= 1
                else:
                    left += 1
            return False

        inorder(root, arr)
        return twoSum(arr, k)