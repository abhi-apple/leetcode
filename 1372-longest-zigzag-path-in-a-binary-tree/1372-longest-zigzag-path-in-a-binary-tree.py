# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        
        def dfs(node,di,le):
            if not node:
                return
            self.maxi=max(le,self.maxi)
            
            if di==0:
                dfs(node.right,not di,le+1)
                dfs(node.left,di,1)
            else:
                dfs(node.left,not di,le+1)
                dfs(node.right,di,1)
            return
                
                
            
            
            
        dfs(root.left,0,1)
        dfs(root.right,1,1)
        return self.maxi