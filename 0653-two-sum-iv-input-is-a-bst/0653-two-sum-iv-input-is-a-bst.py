# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def appendValuesToList(root, values):
            if not root:
                return

            values.append(root.val)

            appendValuesToList(root.left, values)
            appendValuesToList(root.right, values)
        values=[]
        appendValuesToList(root,values)
        seen=set()
        for i in values:
            if k-i in seen:
                return True
            seen.add(i)
        return False

        