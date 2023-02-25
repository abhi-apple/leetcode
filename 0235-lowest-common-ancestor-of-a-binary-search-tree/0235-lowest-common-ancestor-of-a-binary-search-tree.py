# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        
		# Find p/q in left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
		
		# Find p/q in right subtree
        r = self.lowestCommonAncestor(root.right, p, q)
        
		# If p and q found in left and right subtree of this node, then this node is LCA
        if l and r:
            return root
        
		# Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return l if l else r