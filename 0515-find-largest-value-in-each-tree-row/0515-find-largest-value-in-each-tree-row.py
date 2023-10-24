# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que=deque([root])
        if not root:
            return []
        ans=[]
        while que:
            maxi=-float('inf')
            n=len(que)
            for _ in range(n):
                var=que.popleft()
                maxi=max(maxi,var.val)
                if var.left:
                    que.append(var.left)
                if var.right:
                    que.append(var.right)
            ans.append(maxi)
        return ans