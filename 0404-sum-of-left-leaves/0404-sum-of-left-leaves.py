# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def ls(root,c):
            if not root:
                return 0
            if root.left==None and root.right==None and c==True:
                return root.val
            return ls(root.left,True)+ls(root.right,False)
            
        
        return ls(root,False)