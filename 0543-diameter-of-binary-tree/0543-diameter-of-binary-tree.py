# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def heig(root,diam):
            if not root:
                return 0
            lh=heig(root.left,diam)
            rh=heig(root.right,diam)
            diam[0]=max(diam[0],lh+rh)
            return max(lh,rh)+1
        diam=[0]
        heig(root,diam)
        return diam[0]
    