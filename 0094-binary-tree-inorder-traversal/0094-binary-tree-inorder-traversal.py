# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def rec(node):
            if not node:
                return 
            rec(node.left)
            res.append(node.val)
            rec(node.right)
        rec(root)
        return res