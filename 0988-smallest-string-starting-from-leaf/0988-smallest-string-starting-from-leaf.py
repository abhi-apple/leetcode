# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        dic = {}
        for num in range(0, 26):
            dic[num] = chr(ord('a') + num)
        fin=[]
        def dfs(node,val):
            nonlocal fin
            if not node:
                return 
            if not node.left and not node.right:
                val.append(dic[node.val])
                fin.append(''.join(val[::-1]))
                val.pop()
            lft = dfs(node.left,val+[dic[node.val]])
            rgt = dfs(node.right,val+[dic[node.val]])
            
        dfs(root,[])
        return min(fin)

                
            