# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        if not pre:
            return None
        root=TreeNode(pre[0])
        stack=[root]
        for i in range(1,len(pre)):
            node=TreeNode(pre[i])
            if node.val<stack[-1].val:
                stack[-1].left=node
            else:
                while stack and stack[-1].val<node.val:
                    last=stack.pop()
                last.right=node
            stack.append(node)
        return root