# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return 
            if not node.left and not node.right:
                return 1
            if not node.left:
                return rec(node.right)+1
            if not node.right:
                return rec(node.left)+1
            lft=rec(node.left)
            rgt=rec(node.right)
            return min(lft,rgt)+1
        if not rec(root):
            return 0
        return rec(root)
         