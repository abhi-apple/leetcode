# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], que: List[int]) -> List[List[int]]:
        ans = []
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        n = len(ans)
        for q in que:
            left = bisect.bisect_left(ans, q)
            if left == n:
                res.append([ans[-1], -1])
            elif ans[left] == q:
                res.append([q, q])
            elif left == 0:
                res.append([-1, ans[0]])
            else:
                res.append([ans[left-1], ans[left]])
        return res

                
                
        