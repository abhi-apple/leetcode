# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=0
        q=[]
        q.append([root,0])
        while q:
            n=len(q)
            mini=q[0][1]
            las,fir=0,0
            for i in range(n):
                curid=q[0][1]-mini
                node=q[0][0]
                q.pop(0)
                if i==0:
                    fir=curid
                if i==n-1:
                    las=curid
                    
                if node.left:
                    q.append([node.left,2*curid +1])
                if node.right:
                    q.append([node.right,2*curid +2])
                    
            ans=max(ans,las-fir+1)
        return ans