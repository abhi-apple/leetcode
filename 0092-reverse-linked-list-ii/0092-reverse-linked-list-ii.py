# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dum=ListNode(0,head)
        lprev,cur=dum,head
        for i in range(left-1):
            lprev,cur=cur,cur.next
        prev=None
        
        for i in range(right-left+1):
            tmp=cur.next
            cur.next=prev
            prev,cur=cur,tmp
        lprev.next.next=cur
        lprev.next=prev
        return dum.next