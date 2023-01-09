# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def retd(node,ans):
            if node:
                ans.append(node.val)
                retd(node.left,ans)
                retd(node.right,ans)
        ans=[]
        retd(root,ans)
        return ans
    