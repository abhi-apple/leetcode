# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, node, min_val, max_val):
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        left_valid = self.checkBST(node.left, min_val, node.val)
        right_valid = self.checkBST(node.right, node.val, max_val)
        return left_valid and right_valid

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         lft=self.isValidBST(root.left)
#         rgt=self.isValidBST(root.right)
#         if root.left and root.right:
#             if root.left.val<root.val and root.right.val>root.val:
#                 return True
#             else:
#                 return False
#         elif root.left and not root.right:
#             return False
#         elif not root.left and root.right:
#             return False
#         else:
#             return True
        # if root.right:
        #     if root.right.val>root.val:
        #         print( root.right.val,root.val)
        #         return True
        #     else:
        #         return False
        return lft and rgt