"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m,vis,stack=dict(),set(),deque([node])
        while stack:
            n=stack.pop()
            if n in vis:
                continue
            vis.add(n)
            if n not in m:
                m[n]=Node(n.val)
            for nei in n.neighbors:
                if nei not in m:
                    m[nei]=Node(nei.val)
                m[n].neighbors.append(m[nei])
                stack.append(nei)
        return m[node]