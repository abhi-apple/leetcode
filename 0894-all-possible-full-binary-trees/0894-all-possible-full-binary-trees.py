# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def rec(n):
            if n==0 or n & 1==0:
                return []
            if n==1:
                return [TreeNode()]
            res=[]
            for i in range(n):
                r=n-1-i
                lft,rgt=rec(i),rec(r)

                for lt in lft:
                    for rg in rgt:
                        res.append(TreeNode(0,lt,rg))
            return res
        return rec(n)