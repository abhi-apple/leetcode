"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def bst(node):
            if not node:
                return 
            st=[node]
            while st:
                ans=st.pop()
                res.append(ans.val)
                for i in ans.children:
                    st.append(i)
        bst(root)
        return res[::-1]