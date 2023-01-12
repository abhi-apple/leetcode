# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xi=None
        yi=None
        def dfs(node,dep,par):
            nonlocal xi,yi
            if node:
                if node.val==x:
                    xi=(dep,par)
                elif node.val==y:
                    yi=(dep,par)
                dfs(node.left,dep+1,node)
                dfs(node.right,dep+1,node)
        dfs(root,0,None)
        return xi[0]==yi[0] and xi[1]!=yi[1]
        