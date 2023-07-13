# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', B: 'TreeNode', A: 'TreeNode') -> 'TreeNode':
        def rec(node,p,q):
            if not node or node==p or node==q:
                return node
            lft=rec(node.left,p,q)
            rgt=rec(node.right,p,q)
            if not lft:
                return rgt
            elif not rgt:
                return lft
            else:
                return node
        return rec(root,A,B)
                
                