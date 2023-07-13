# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        stack=deque([(root,1)])
        while stack:
            n=len(stack)
            st=stack[0][1]
            
            for _ in range(n):
                node,val=stack.popleft()
                ed=val
                if node.left:
                    stack.append([node.left,(2*val)])
                if node.right:
                    stack.append([node.right,(2*val)+1])
            maxi=max(maxi,ed-st+1)
        return maxi
                