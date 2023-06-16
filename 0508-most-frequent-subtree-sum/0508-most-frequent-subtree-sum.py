# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        fin=[]
        res=[]
        def dfs(node):
            if not node:
                return 0
            lft=dfs(node.left)
            rgt=dfs(node.right)
            fin.append(lft+rgt+node.val)
            return lft+rgt+node.val
        dfs(root)
        maxi=1
        final=set(fin)
        print(fin)
        for i in final:
            cnt=fin.count(i)
            if cnt>maxi:
                res=[i]
                maxi=cnt
            elif cnt==maxi:
                res.append(i)
                
        return res
            