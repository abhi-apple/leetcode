# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(node,currmax,currmin):
            if not node:
                return currmax-currmin
            currmax=max(currmax,node.val)
            currmin=min(currmin,node.val)
            left=helper(node.left,currmax,currmin)
            right=helper(node.right,currmax,currmin)
            return max(left,right)
        return helper(root,root.val,root.val)