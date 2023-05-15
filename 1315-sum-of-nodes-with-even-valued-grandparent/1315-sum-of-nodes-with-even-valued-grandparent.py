# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sums=0
        def rec(node):
            if not node:
                return
            nonlocal sums
            if node.val & 1==0:
                if node.left:
                    if node.left.right:
                        sums+=node.left.right.val
                    if node.left.left:
                        sums+=node.left.left.val
                if node.right:
                    if node.right.right:
                        sums+=node.right.right.val
                    if node.right.left:
                        sums+=node.right.left.val
            rec(node.left)
            rec(node.right)
        rec(root)
        return sums