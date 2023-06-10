# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = {}
        deq = deque([(root, 0)])  # Store (node, val) tuples in the deque
        
        while deq:
            node, val = deq.popleft()
            

            nodes[val] = node.val
            
            if node.left:
                deq.append((node.left, val + 1))  # Append (node, val) tuple to the deque
            if node.right:
                deq.append((node.right, val + 1))  # Append (node, val) tuple to the deque
        
        return [nodes[i] for i in sorted(nodes)]
                
            
                