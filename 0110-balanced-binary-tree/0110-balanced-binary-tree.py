# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return height(root) != -1
#         ans=True
#         def res(root):
#             if root==None:
#                 return 0
#             lh=res(root.left)+1
#             th=res(root.right)+1
#             if abs(lh-th)>1:
#                 ans=False
            
            
            
#         return ans