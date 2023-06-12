# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node,maxi,mini):
            if not node:
                return True
            lft=rec(node.left,node.val,mini)
            rgt=rec(node.right,maxi,node.val)
            if node.val<maxi and node.val>mini:
                return lft and rgt
            else:
                return False
        return rec(root,float('inf'),-float('inf'))