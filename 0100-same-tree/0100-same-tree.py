# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=True
        def rec(n1,n2):
            nonlocal ans
            if not n1 and not n2:
                return 
            if not n1 or not n2:
                ans=False
                return 
            if n1.val!=n2.val:
                ans=False
                return
            rec(n1.left,n2.left)
            rec(n1.right,n2.right)
            return
        rec(p,q)
        return ans