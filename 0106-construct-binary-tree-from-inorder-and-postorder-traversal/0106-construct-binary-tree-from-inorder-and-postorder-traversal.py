# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, ino: List[int], pos: List[int]) -> Optional[TreeNode]:
        if not ino or not pos:
            return None
        rootval=pos.pop()
        rooti=ino.index(rootval)
        root=TreeNode(rootval)
        root.right=self.buildTree(ino[rooti+1:],pos)
        root.left=self.buildTree(ino[:rooti],pos)
        
        return root
        