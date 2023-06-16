# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        fin=False
        
        def dfs(node):
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
            nonlocal fin
            if not node:
                return None
            rec(node,subRoot)
            if ans:
                fin=True
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return fin
            