# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        que=[root]
        lftr=True
        while que:
            row=[]
            for i in range(len(que)):
                node=que.pop(0)
                row.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            if lftr:
                res.append(row)
            else:
                res.append(row[::-1])
                
            lftr= not lftr
            
        return res

                    