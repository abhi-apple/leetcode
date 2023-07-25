# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        main=0
        def rec(node):
            
            nonlocal main
            if not node:
                return 0
        
            lft=rec(node.left)
            rgt=rec(node.right)
            lftpar=lft+1 if node.left and  node.left.val==node.val else 0
            rgtpar=rgt+1 if node.right and node.right.val==node.val else 0
   
            main=max(main,lftpar+rgtpar)
            return max(lftpar,rgtpar)
        rec(root)
        return main