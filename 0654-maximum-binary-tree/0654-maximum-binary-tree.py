# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(arr):
            if not arr:
                return 
            maxi=max(arr)
            ind=arr.index(maxi)
            node=TreeNode(maxi)
            node.left=rec(arr[:ind])
            node.right=rec(arr[ind+1:])
            return node
            

        return rec(nums)