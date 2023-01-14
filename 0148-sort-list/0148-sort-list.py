# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        val=[]
        cur=head
        while cur:
            val.append(cur.val)
            cur=cur.next
        val.sort()
        cur=head
        for v in val:
            cur.val=v
            cur=cur.next
        return head