# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dumm=ListNode(0)
#         dumm.next=head
#         lft=dumm
#         rgt=dumm.next
#         while n<0 and rgt:
#             rgt=rgt.next
#             n-=1
#         while rgt:
#             lft=lft.next
#             rgt=rgt.next
            
#         lft.next=lft.next.next
#         return dumm.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumm = ListNode(0)
        dumm.next = head
        lft = dumm
        rgt = dumm.next
        while n > 0 and rgt:
            rgt = rgt.next
            n -= 1
        while rgt:
            lft = lft.next
            rgt = rgt.next
        lft.next = lft.next.next
        return dumm.next

