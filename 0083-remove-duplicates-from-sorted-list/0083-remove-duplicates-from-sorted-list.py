# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(101)
        dum.next=head
        prev,cur=dum,head
        while cur:
            nxt=cur.next
            if cur.val==prev.val:
                prev.next=nxt
            else:
                prev=cur
            cur=nxt
        return dum.next