# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        lev=0
        que=[]
        que.append(root)
        while que:
            for i in range(len(que)):
                node=que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            lev+=1
        return lev
        
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        