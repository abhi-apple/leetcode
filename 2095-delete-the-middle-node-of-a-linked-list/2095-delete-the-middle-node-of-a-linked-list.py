# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        dumm=ListNode(0,head)
        fir=dumm.next
        if not fir.next:
            return None
        while fir.next!=slow:
            fir=fir.next
        fir.next=fir.next.next
        return dumm.next
            