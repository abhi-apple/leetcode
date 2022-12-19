# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        befh=ListNode(0)
        afth=ListNode(0)
        
        bef=befh
        aft=afth
        while head:
            if head.val<x:
                bef.next=head
                bef=bef.next
            else:
                aft.next=head
                aft=aft.next
            head=head.next
        aft.next=None
        
        bef.next=afth.next
        return befh.next