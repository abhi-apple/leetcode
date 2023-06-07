# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next=ListNode(l1.val)
                l1=l1.next
            else:
                tail.next=ListNode(l2.val)
                l2=l2.next
                
            tail=tail.next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        return dummy.next