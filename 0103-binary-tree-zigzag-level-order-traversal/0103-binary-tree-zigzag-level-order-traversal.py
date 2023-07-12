# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final=[]
        if not root:
            return []
        st=True
        stack=deque([root])
        while stack:
            n=len(stack)
            ans=[]
            for _ in range(n):
                node=stack.popleft()
                ans.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if st:
                final.append(ans)
                
            else:
                final.append(ans[::-1])
            st=not st
        return final
                
                    