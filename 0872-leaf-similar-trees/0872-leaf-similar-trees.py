# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def lf(node,v):
            if not node:
                return
            if not node.right and not node.left:
                v.append(node.val)
            lf(node.left,v)
            lf(node.right,v)
            
        v1=[]
        v2=[]
        lf(root1,v1)
        lf(root2,v2)
        if v1==v2:
            return True
        return False