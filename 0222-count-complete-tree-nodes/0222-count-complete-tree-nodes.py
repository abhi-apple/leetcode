# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def fnd(node):
            hgtl=0
            while node:
                hgtl+=1
                node=node.left
            return hgtl
        def fndr(node):
            hgtr=0
            while node:
                hgtr+=1
                node=node.right
            return hgtr
        
        lh=fnd(root)
        rh=fndr(root)
        if rh==lh:
            return (1<<lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    