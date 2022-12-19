# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        sta=[[root,1]]
        res=0
        while sta:
            node,dep=sta.pop()
            if node:
                res=max(res,dep)
                sta.append([node.left,dep+1])
                sta.append([node.right,dep+1])
        return res
        # lev=0
        # que=[]
        # que.append(root)
        # while que:
        #     for i in range(len(que)):
        #         node=que.pop(0)
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        #     lev+=1
        # return lev
        
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        