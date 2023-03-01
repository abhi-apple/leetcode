# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dep(node):
            if not node:
                return 0
            l=dep(node.left)
            r=dep(node.right)
            self.ans=max(self.ans,l+r+1)
            return max(l,r)+1
        dep(root)
        return self.ans-1