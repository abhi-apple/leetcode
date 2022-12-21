# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sums=0
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.right
            curr=stack.pop()
            sums+=curr.val
            curr.val=sums
            curr=curr.left
        return root