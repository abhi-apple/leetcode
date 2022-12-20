# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        elem=[]
        def inor(node):
            if not node:
                return 
            inor(node.left)
            elem.append(node.val)
            inor(node.right)
        inor(root)
        if len(elem)==1:
            return elem[0]
        mini=elem[1]-elem[0]
        for i in range(1,len(elem)):
            dif=elem[i]-elem[i-1]
            mini=min(dif,mini)
        return mini