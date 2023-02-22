# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        path=[]
        cnt=0
        def solve(node):
            nonlocal path
            nonlocal cnt
            if not node:
                return 
            path.append(node.val)
            solve(node.left)
            solve(node.right)
            sums=0
            for i in reversed(path):
                sums+=i
                if sums==k:
                    cnt+=1
            path.pop()
            
        solve(root)
        return cnt