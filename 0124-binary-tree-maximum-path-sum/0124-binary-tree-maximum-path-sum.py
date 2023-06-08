# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=-1000
        def rec(node):
            nonlocal maxi
            if not node:
                return 0
            lft=max(0,rec(node.left))
            rgt=max(0,rec(node.right))
            maxi=max(maxi,lft+rgt+node.val)
            return max(lft,rgt)+node.val
        rec(root)
        return maxi