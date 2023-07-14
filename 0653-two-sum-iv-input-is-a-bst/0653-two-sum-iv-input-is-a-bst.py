# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        store=set()
        def rec(node):
            nonlocal store
            if not node:
                return False
            lft=rec(node.left)
            rgt=rec(node.right)
            if k-node.val in store:
                return True
            store.add(node.val)
            return lft or rgt
        return rec(root)
            
            