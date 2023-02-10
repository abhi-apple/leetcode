# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=ListNode(0,head)
        lef=dum
        rig=dum.next
        while n>0 and rig:
            rig=rig.next
            n-=1
        while rig:
            lef=lef.next
            rig=rig.next
        lef.next=lef.next.next
        return dum.next
            