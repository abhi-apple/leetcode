# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def rec(node):
            nonlocal maxi
            if not node:
                return 0
            lft=rec(node.left)
            rgt=rec(node.right)
            maxi=max(maxi,lft+rgt+1)
            return max(lft,rgt)+1
        rec(root)
        return maxi-1