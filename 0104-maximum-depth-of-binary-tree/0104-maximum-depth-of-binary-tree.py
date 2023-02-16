# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def res(root):
            if root==None:
                return 0
            left=res(root.left)+1
            right=res(root.right)+1
            return max(left,right)
        
        
        
        return res(root)
        