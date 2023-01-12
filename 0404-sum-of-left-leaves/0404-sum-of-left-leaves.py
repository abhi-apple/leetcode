# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums=0
        def ls(root,c):
            if not root:
                return 0
            if root.left==None and root.right==None and c==True:
                return root.val
            lf=ls(root.left,True)
            rt=ls(root.right,False)
            return lf+rt
            
        
        return ls(root,False)