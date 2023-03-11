# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        ans=[]
        while head :
            ans.append(head.val)
            head=head.next
        def sortedArrayToBST(nums):
            
            if not nums:
                return None
            # Find middle element
            mid = len(nums) // 2
            # Create new TreeNode for middle element
            root = TreeNode(nums[mid])
            # Construct left subtree
            root.left = sortedArrayToBST(nums[:mid])
            # Construct right subtree
            root.right = sortedArrayToBST(nums[mid+1:])
            return root
        return sortedArrayToBST(ans)