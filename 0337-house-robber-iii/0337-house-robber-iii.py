# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={}
        def rec(node):
            if not node:
                return [0,0]
            if node in dp:
                return dp[node]
            maxi=0
            witr=node.val+rec(node.left)[1]+rec(node.right)[1]
            wito=max(rec(node.left))+max(rec(node.right))
            dp[node]=[witr,wito]
            return dp[node]
        
        return max(rec(root))
            