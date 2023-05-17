# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt=0
        def rec(node,maxi):
            nonlocal cnt
            if not node:
                return 
            if node.val>=maxi:
                cnt+=1
                maxi=node.val
            rec(node.left,maxi)
            rec(node.right,maxi)
            return
        
                
            
            
        rec(root,root.val)
        return cnt