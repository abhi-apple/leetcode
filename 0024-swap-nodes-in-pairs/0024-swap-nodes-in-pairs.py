# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0,head)
        prev=dum
        cur=head
        while cur and cur.next:
            nxt = cur.next.next
            prev.next = cur.next
            cur.next.next = cur
            cur.next = nxt
            prev = cur
            cur = nxt
        return dum.next
            
        