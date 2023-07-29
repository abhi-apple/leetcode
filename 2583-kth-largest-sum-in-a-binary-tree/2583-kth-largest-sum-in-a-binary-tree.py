# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        maxi=[]
        que=deque()
        que.append(root)
        while que:
            n=len(que)
            sums=0
            for _ in range(n):
                node=que.popleft()
                sums+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            maxi.append(sums)
        if len(maxi)<k:
            return -1
        maxi.sort(reverse=True)
        return maxi[k-1]
                