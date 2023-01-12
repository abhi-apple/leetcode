# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        curr=set()
        def fd(root,res,curr,v):
            if not root:
                return
            if v not in curr:
                curr.add(v)
                res.append(root.val)
            fd(root.right,res,curr,v+1)
            fd(root.left,res,curr,v+1)
        
        fd(root,res,curr,0)
        return res