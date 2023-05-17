# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return 0

            left_sum = rec(node.left)
            right_sum = rec(node.right)
            
            if left_sum == 0 and node.left:
                node.left = None
            
            if right_sum == 0 and node.right:
                node.right = None
                
            return left_sum + right_sum + node.val
        
        if rec(root) == 0:
            return None
        
        return root

        