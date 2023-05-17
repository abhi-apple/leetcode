# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], td: List[int]) -> List[TreeNode]:
        td=set(td)
        res=set()
        def rec(node):
            nonlocal res
            if not node:
                return None
            node.left=rec(node.left)
            node.right=rec(node.right)
            if node.val in td:
                if node.left:
                    res.add(node.left)
                if node.right:
                    res.add(node.right)
                return None
            return node
        if root.val not in td:
            res.add(rec(root))
        else:
            rec(root)
        return res
        
        