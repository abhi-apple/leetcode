# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree=root
        self.ans=[]
        def rec(node):
            if not node:
                return None
            rec(node.left)
            self.ans.append(node.val)
            rec(node.right)
        rec(root)
        

    def next(self) -> int:
        res=self.ans[0]
        self.ans=self.ans[1:]
        return res

    def hasNext(self) -> bool:
        if self.ans:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()