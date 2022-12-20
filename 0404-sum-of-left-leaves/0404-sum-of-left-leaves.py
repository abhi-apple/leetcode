# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sums=0
        que=[root]
        while que:
            node=que.pop(0)
            if node.left and not node.left.left and not node.left.right:
                sums+=node.left.val
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return sums