# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if not root:
#             return None
#         def findrgt(node):
#             if not node.right:
#                 return node
#             return findrgt(node.right)
#         def helper(node):
#             if not node.left:
#                 return node.right
#             elif not root.right:
#                 return root.left
#             rgtch=root.right
#             lastr=findrgt(node.left)
#             lastr.right=rgtch
#             return node.left
#         if root.val==key:
#             return helper(root)
#         dummy=root
#         while root:
#             if root.val>key:
#                 if root.left and root.left.val==key:
#                     root.left=helper(root.left)
#                     break
                    
#                 else:
                    
#                     root=root.left
#             else:
#                 if root.right and root.right.val==key:
#                     root.right=helper(root.right)
#                     break
#                 else:
#                     root=root.right
#         return dummy


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self.helper(root)

        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return dummy

    def helper(self, root: TreeNode) -> Optional[TreeNode]:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        rightChild = root.right
        lastRight = self.findLastRight(root.left)
        lastRight.right = rightChild
        return root.left

    def findLastRight(self, root: TreeNode) -> Optional[TreeNode]:
        if not root.right:
            return root
        return self.findLastRight(root.right)
