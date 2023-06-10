# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', B: 'TreeNode', A: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, arr,com):
            if not node:
                return None
            if node == com:
                return arr + [com]
            left_result = dfs(node.left, arr + [node],com)
            right_result = dfs(node.right, arr + [node],com)
            return left_result or right_result
        
        ans=dfs(root, [],A)
        
        res=dfs(root,[],B) 
        # print(ans,res)
        for i in range(min(len(ans),len(res))-1,-1,-1):
            if ans[i]==res[i]:
                return ans[i]
        return ans[0]