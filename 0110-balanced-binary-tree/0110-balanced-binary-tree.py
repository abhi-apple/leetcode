# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def hei(node):
            if not node:
                return 0
            lft=hei(node.left)
            rgt=hei(node.right)
            if lft==-1 or rgt==-1:
                return -1
            if abs(lft-rgt)>1:
                return -1
            return max(lft,rgt)+1
        if hei(root)==-1:
            return False
        return True
            
#         ans=True
#         def res(root):
#             if root==None:
#                 return 0
#             lh=res(root.left)+1
#             th=res(root.right)+1
#             if abs(lh-th)>1:
#                 ans=False
            
            
            
#         return ans