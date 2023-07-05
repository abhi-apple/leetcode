# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        od=ListNode(head.val)
        odhead=od
        ev=ListNode(head.next.val)
        evhead=ev
        cur=head.next.next
        while cur and cur.next:
            
            od.next=ListNode(cur.val)
            ev.next=ListNode(cur.next.val)
            od=od.next
            ev=ev.next
            cur=cur.next.next

        if cur:
            od.next=ListNode(cur.val)
            od=od.next
        od.next=evhead
        return odhead
       
            

        
        
            
            
        
        
        