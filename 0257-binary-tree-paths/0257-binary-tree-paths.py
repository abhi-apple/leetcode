# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def path(root,res,curr):
            if not root:
                return 
            if root.left==None and root.right==None:
                curr+=str(root.val)
                res.append(curr)
            curr+=str(root.val)+'->'
            if root.left:
                path(root.left,res,curr)
            if root.right:
                path(root.right,res,curr)
                
        
        path(root,res,'')
        return res