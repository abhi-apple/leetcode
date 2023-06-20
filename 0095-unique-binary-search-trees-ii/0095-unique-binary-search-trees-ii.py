# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        main=list(range(1,n+1))
        def dfs(nums):
            if not nums:
                return [None]
            ans=[]
            for i in range(len(nums)):
                lft=dfs(nums[:i])
                rgt=dfs(nums[i+1:])
                for l in lft:
                    for r in rgt:
                        root=TreeNode(nums[i])
                        root.left=l
                        root.right=r
                        ans.append(root)
            return ans
        return dfs(main)
                