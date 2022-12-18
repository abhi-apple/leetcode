# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxi=nums.index(max(nums))
        root=TreeNode(nums[maxi])
        root.left=self.constructMaximumBinaryTree(nums[:maxi])
        root.right=self.constructMaximumBinaryTree(nums[maxi+1:])
        return root
        