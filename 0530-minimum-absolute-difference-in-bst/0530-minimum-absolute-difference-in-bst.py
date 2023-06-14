# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini=float('inf')
        res=deque()
        def rec(node):
            nonlocal res,mini
            if not node:
                return None
            rec(node.left)
            if node:
                res.append(node.val)
                if len(res)>1:
                    lft=res.popleft()
                    mini=min(mini,res[-1]-lft)
                
            rec(node.right)
                    
            
            
        rec(root)
        return mini