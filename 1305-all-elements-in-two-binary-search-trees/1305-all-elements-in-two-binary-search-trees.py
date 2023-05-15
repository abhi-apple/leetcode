# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res=[]
        def rec(node):
            if not node :
                return 
            res.append(node.val)
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)
            return 
        rec(root1)
        rec(root2)
        res.sort()
        return res