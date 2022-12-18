# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxd=0
        sums=0
        
        def dfs(node,dep):
            nonlocal maxd
            nonlocal sums
            if dep>maxd:
                maxd=dep
                sums=node.val
            elif dep==maxd:
                sums+=node.val
            if node.left:
                dfs(node.left,dep+1)
            if node.right:
                dfs(node.right,dep+1)
        dfs(root,1)
        return sums