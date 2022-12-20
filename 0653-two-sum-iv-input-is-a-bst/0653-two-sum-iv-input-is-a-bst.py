# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        elem=[]
        def inor(node):
            if not node:
                return 
            inor(node.left)
            elem.append(node.val)
            inor(node.right)
        inor(root)
        left=0
        rgt=len(elem)-1
        while left<rgt:
            if elem[left]+elem[rgt]==k:
                return True
            elif elem[left]+elem[rgt]<k:
                left+=1
            else:
                rgt-=1
        return False
#         def appendValuesToList(root, values):
#             if not root:
#                 return

#             values.append(root.val)

#             appendValuesToList(root.left, values)
#             appendValuesToList(root.right, values)
#         values=[]
#         appendValuesToList(root,values)
#         seen=set()
#         for i in values:
#             if k-i in seen:
#                 return True
#             seen.add(i)
#         return False

        