# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}
        que = deque([(root, 0, 0)])  # (node, (vertical, level))
        while que:
            node,x,y=que.popleft()
            if x not in nodes:
                nodes[x]={}
            if y not in nodes[x]:
                nodes[x][y]=[]
            nodes[x][y].append(node.val)
            if node.left:
                que.append([node.left,x-1,y+1])
            if node.right:
                que.append([node.right,x+1,y+1])
        ans=[]
        for col in sorted(nodes.keys()):
            cold=[]
            for row in sorted(nodes[col].keys()):
                cold.extend(sorted(nodes[col][row]))
            ans.append(cold)
        return ans