# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def rec(node):
            if not node:
                return 0
            return 1+max(rec(node.left),rec(node.right))
        lft=rec(root.left)
        rgt=rec(root.right)
        if lft==rgt:
            return root
        else:
            if lft>rgt:
                return self.lcaDeepestLeaves(root.left)
            return self.lcaDeepestLeaves(root.right)