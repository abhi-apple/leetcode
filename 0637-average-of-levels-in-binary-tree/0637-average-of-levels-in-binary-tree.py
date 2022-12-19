# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        if not root:
            return 0
        que=[]
        que.append(root)
        print(len(que))
        
        while que:
            levs=len(que)
            levsum=0
            for i in range(levs):
                curn=que.pop(0)
                levsum+=curn.val
                if curn.left:
                    que.append(curn.left)
                if curn.right:
                    que.append(curn.right)
                    
            res.append(levsum/levs)
        return res
        # while que:
            
        