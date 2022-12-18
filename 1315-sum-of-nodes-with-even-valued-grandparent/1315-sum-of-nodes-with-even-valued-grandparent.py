# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.t=0
        
        def dfs(root):
            if root.val%2==0:
                if root.left:
                    if  root.left.left:
                        self.t+=root.left.left.val
                    if  root.left.right:
                        self.t+= root.left.right.val
                if root.right:
                    if  root.right.left:
                        self.t+=root.right.left.val
                    if  root.right.right:
                        self.t+=root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return
        dfs(root)
        return self.t