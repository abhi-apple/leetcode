# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        if n==1:
            return [TreeNode(0)]
        trees=[]
        for i in range(1,n,2):
            leftt=self.allPossibleFBT(i)
            rightt=self.allPossibleFBT(n-i-1)
            for lef in leftt:
                for rig in rightt:
                    root=TreeNode(0)
                    root.left=lef
                    root.right=rig
                    trees.append(root)
        return trees