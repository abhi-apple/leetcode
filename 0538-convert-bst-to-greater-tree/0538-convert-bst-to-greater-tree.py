# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums=0
        
        def rec(node):
            nonlocal sums
            if not node:
                return 0
            rec(node.right)
            node.val+=sums
            sums=node.val
            rec(node.left)
        rec(root)
        return root
            
            