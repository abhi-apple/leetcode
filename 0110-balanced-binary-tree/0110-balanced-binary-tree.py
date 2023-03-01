# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def hei(node):
            if not node:
                return 0
            lft=hei(node.left)
            rgt=hei(node.right)
            return max(lft,rgt)+1
        lft=self.isBalanced(root.left)
        rgt=self.isBalanced(root.right)
        diff=True if abs(hei(root.left)-hei(root.right))<=1 else False
        if lft and rgt and diff:
            return True
        else:
            False
            
#         ans=True
#         def res(root):
#             if root==None:
#                 return 0
#             lh=res(root.left)+1
#             th=res(root.right)+1
#             if abs(lh-th)>1:
#                 ans=False
            
            
            
#         return ans