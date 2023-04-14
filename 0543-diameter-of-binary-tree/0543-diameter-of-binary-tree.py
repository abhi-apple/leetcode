# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def dfs(node):
            if not node:
                return 0
            lft=dfs(node.left)
            rgt=dfs(node.right)
            dia=lft+rgt
            self.maxi=max(self.maxi,dia)
            return max(lft,rgt)+1
        dfs(root)
        return self.maxi
        
        # def hei(node):
        #     if not node:
        #         return 0
        #     return max(hei(node.left),hei(node.right))+1
        # if not root:
        #     return 0
        # op1=self.diameterOfBinaryTree(root.left)
        # op2=self.diameterOfBinaryTree(root.right)
        # op3=hei(root.left)+hei(root.right)+1
        # return max(op1,op2,op3)
        