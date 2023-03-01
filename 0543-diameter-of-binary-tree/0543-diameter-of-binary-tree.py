# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node):
            if not node:
                return (0, 0)
            left_height, left_diameter = diameter(node.left)
            right_height, right_diameter = diameter(node.right)
            current_diameter = left_height + right_height
            max_diameter = max(left_diameter, right_diameter, current_diameter)
            return (max(left_height, right_height) + 1, max_diameter)

        return diameter(root)[1]

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def hei(node):
#             if not node:
#                 return 0
#             return max(hei(node.left),hei(node.right))+1
#         if not root:
#             return 0
#         op1=self.diameterOfBinaryTree(root.left)
#         op2=self.diameterOfBinaryTree(root.right)
#         op3=hei(root.left)+hei(root.right)+1
#         return max(op1,op2,op3)
        