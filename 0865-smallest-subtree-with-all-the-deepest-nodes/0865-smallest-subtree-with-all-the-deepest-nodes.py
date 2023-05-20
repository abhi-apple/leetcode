# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        def geth(node):
            if not node:
                return 0
            return 1+max(geth(node.left),geth(node.right))
        lft=geth(root.left)
        rgt=geth(root.right)
        if lft==rgt:
            return root
        else:
            if lft>rgt:
                return self.subtreeWithAllDeepest(root.left)
            else:
                return self.subtreeWithAllDeepest(root.right)
        
        