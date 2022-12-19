# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, ori: TreeNode, cl: TreeNode, tar: TreeNode) -> TreeNode:
        if ori is None or cl is None:
            return None
        if ori==tar:
            print(cl)
            return cl
        left=self.getTargetCopy(ori.left,cl.left,tar)
        if left is not None:
            return left
        right=self.getTargetCopy(ori.right,cl.right,tar)
        if right is not None:
            return right
        return None