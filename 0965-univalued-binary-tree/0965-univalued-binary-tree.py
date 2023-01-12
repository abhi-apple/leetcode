# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ans=root.val
        def ism(root,ans):
            if not root:
                return True
            if root.val!=ans:
                return False
            left=ism(root.left,ans)
            rg=ism(root.right,ans)
            return left and rg
        return ism(root,ans)