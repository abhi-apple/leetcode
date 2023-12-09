class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def rec(node):
            if not node:
                return 
            rec(node.left)
            res.append(node.val)
            rec(node.right)
        rec(root)
        return res