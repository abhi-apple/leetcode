"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        st=[[root,1]]
        maxd=0
        while st:
            node,dep=st.pop()
            maxd=max(maxd,dep)
            for ch in node.children:
                st.append([ch,dep+1])
        return maxd
        # maxd=0
        # for ch in root.children:
        #     maxd=max(self.maxDepth(ch),maxd)
        # return maxd+1