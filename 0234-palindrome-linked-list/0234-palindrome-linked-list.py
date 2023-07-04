# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        def rev(node):
            prev=None
            nxt=None
            while node!=None:
                nxt=node.next
                node.next=prev
                prev=node
                node=nxt
                
            return prev
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=rev(slow.next)
        slow=slow.next
        
        dumm=head
        while slow!=None:
            if slow.val!=dumm.val:
                return False
            slow=slow.next
            dumm=dumm.next
        return True
            
            
            