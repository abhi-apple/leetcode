# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
        
#         """
#         st=''
#         def bfs(node):
#             nonlocal st
#             if not node:
#                 return '#'
#             que=deque([node])
#             st+=str(node.val)
#             while que:
#                 now=que.popleft()
#                 if now.left:
#                     que.append(now.left)
#                     st+=str(now.left.val)
#                 else:
#                     st+='#'
#                 if now.right:
#                     que.append(now.right)
#                     st+=str(now.right.val)
#                 else:
#                     st+='#'
#         bfs(root)
#         print(st)
#         return st

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
        
#         """
#         if not data:
#             return None
#         root=TreeNode(int(data[0]))
#         que=deque([root])
#         data=list(data)
#         data=data[1:]
#         while que:
#             node=que.popleft()
#             if data[0]=='#':
#                 node.left=None
#             else:
#                 node.left=TreeNode(int(data[0]))
#                 que.append(node.left)
#             data.pop(0)
#             if data[0]=='#':
#                 node.right=None
#             else:
#                 node.right=TreeNode(int(data[0]))
#                 que.append(node.right)
#             data.pop(0)
            
#         return root
from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ''

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        values = data.split()
        root_val = int(values[0])
        root = TreeNode(root_val)
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] != '#':
                left_val = int(values[i])
                node.left = TreeNode(left_val)
                queue.append(node.left)
            i += 1

            if values[i] != '#':
                right_val = int(values[i])
                node.right = TreeNode(right_val)
                queue.append(node.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))