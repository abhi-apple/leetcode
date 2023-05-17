# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], tar: int) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return 
            node.left=rec(node.left)
            node.right=rec(node.right)
            
            if not node.left and not node.right and node.val==tar:
                node=None

            return node
        return rec(root)
    
        
            