# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        que=deque([root])
        if depth==1:
            fin=TreeNode(val)
            fin.left=root
            return fin
        cnt=1
        while que:
            n=len(que)
            
            if cnt==depth-1:
                for _ in range(n):
                    var=que.popleft()
                    st1=var.left
                    st2=var.right
                    var.left=TreeNode(val)
                    var.right=TreeNode(val)
                    var.left.left=st1
                    var.right.right=st2
                return root
            else:
                cnt+=1
                for _ in range(n):
                    var=que.popleft()
                    if var.left:
                        que.append(var.left)
                    if var.right:
                        que.append(var.right)
        return root
                
                    
                