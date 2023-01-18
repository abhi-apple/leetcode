# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        sums=0
        que=[(root,0)]
        while que:
            node,lev=que.pop(0)
            if node.val & 1==0:
                if node.left:
                    if node.left.right:
                        lev+=node.left.right.val
                    if node.left.left:
                        lev+=node.left.left.val
                if node.right:
                    if node.right.right:
                        lev+=node.right.right.val
                    if node.right.left:
                        lev+=node.right.left.val
            sums+=lev
            if node.left:
                que.append((node.left,0))
            if node.right:
                que.append((node.right,0))
        return sums
                    