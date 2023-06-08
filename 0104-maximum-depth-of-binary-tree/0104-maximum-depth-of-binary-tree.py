# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return 0
            nl=rec(node.left)
            rl=rec(node.right)
            return max(nl,rl)+1
        return rec(root)