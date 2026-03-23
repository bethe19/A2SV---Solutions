# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        post_idx = 0
        
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            while stack[-1].val == postorder[post_idx]:
                stack.pop()
                post_idx += 1
                
            parent = stack[-1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
                
            stack.append(node)
            
        return root

            
