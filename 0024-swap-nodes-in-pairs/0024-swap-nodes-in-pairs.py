# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            dum=ListNode(0,head)
            prev,cur=dum,head
            while cur and cur.next:
                nxtp=cur.next.next
                sec=cur.next
                sec.next=cur
                cur.next=nxtp
                prev.next=sec
                prev=cur
                cur=nxtp
            return dum.next
                