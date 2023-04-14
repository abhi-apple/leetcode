# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def bfs(root):
            if not root:
                return []
            que=[root]
            while que:
                levs=len(que)
                cur=[]
                for i in range(levs):
                    node=que.pop(0)
                    cur.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
           
                res.append(cur[-1])
     
                
            return res
 
        return bfs(root)
                
                