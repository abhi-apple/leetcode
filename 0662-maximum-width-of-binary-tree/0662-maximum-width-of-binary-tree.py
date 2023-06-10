# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # Store (node, index) tuples in the queue
        
        while queue:
            
            level_size = len(queue)
            _, start_index = queue[0]  # Leftmost node index at current level
            _, end_index = queue[-1]  # Rightmost node index at current level

            max_width = max(max_width, end_index - start_index + 1)
            
            for _ in range(level_size):
                
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width
            