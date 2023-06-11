# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return TreeNode(val)  # Create a new node if the current node is None
            if node.val > val:
                node.left = rec(node.left)  # Assign the returned node to node.left
            else:
                node.right = rec(node.right)  # Assign the returned node to node.right
            return node
        
        return rec(root)

                