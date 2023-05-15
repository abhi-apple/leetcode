# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        cnt=0
        def rec(node):
            nonlocal cnt
            if not node:
                return [0,0]
            l=rec(node.left)
            r=rec(node.right)
            if (l[0]+r[0]+node.val)//(l[1]+r[1]+1)==node.val:
                cnt+=1
                
            return [l[0]+r[0]+node.val,l[1]+r[1]+1]
        rec(root)
        return cnt