# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, des: List[List[int]]) -> Optional[TreeNode]:
        dic={}
        vis=set()
        for par,ch,dire in des:
            if par not in dic:
                dic[par]=TreeNode(par)
            if ch not in dic:
                dic[ch]=TreeNode(ch)
            if dire:
                dic[par].left=dic[ch]
            else:
                dic[par].right=dic[ch]
            vis.add(ch)
        for i in dic:
            if i not in vis:
                return dic[i]
        return []
    
    
  