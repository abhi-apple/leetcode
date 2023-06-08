# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def rec(node):
            nonlocal ans
            if not node:
                return 0

            left_height = rec(node.left)
            right_height = rec(node.right)

            if abs(left_height - right_height) > 1:
                ans = False

            return max(left_height, right_height) + 1

        rec(root)
        return ans
