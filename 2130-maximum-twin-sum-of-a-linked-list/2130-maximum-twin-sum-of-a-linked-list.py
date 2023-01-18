# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sl=fas=head
        sums=0
        while fas:
            sl=sl.next
            fas=fas.next.next
        curr,prev=sl,None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next 
        while prev:
            sums=max(sums,prev.val+head.val)
            prev=prev.next
            head=head.next
        return sums
            