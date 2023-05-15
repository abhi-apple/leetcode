# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        maxi = float('inf')
        i = 0

        def bst(bnd, ind):
            nonlocal i
            if ind == len(pre) or pre[ind] > bnd:
                return None

            root = TreeNode(pre[ind])
            i += 1
            root.left = bst(root.val, i)
            root.right = bst(bnd, i)
            return root

        return bst(maxi, i)

        