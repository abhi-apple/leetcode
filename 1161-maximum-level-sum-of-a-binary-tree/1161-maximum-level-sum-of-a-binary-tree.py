# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        que=deque([root])
        sums=-float('inf')
        cnt=0
        finl=0
        while que:
            n=len(que)
            cnt+=1
            val=0
            for _ in range(n):
                
                var=que.popleft()
                val+=var.val
                if var.left:
                    que.append(var.left)
                if var.right:
                    que.append(var.right)
            print('brk')
            if val>sums:
                sums=val
                finl=cnt
        return finl