# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic={}
        res=[]
        def re(node,path):
            if not node:
                return '#'
            path=','.join([str(node.val),re(node.left,path),re(node.right,path)])
            if path in dic:
                dic[path]+=1
                if dic[path]==2:
                    res.append(node)
            else:
                dic[path]=1
            return path
        re(root,'')
        
        return res