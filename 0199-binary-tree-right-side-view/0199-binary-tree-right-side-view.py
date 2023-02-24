# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def ans(node,l):
            nonlocal res
            if not node:
                return 
            if l==len(res):
                res.append(node.val)
            ans(node.right,l+1)
            ans(node.left,l+1)
            
            
            
        ans(root,0)
        return res