# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f=''
        l=''
        while l1:
            f=str(l1.val)+f
            l1=l1.next
        while l2:
            l=str(l2.val)+l
            l2=l2.next
        fin=int(f)+int(l)
        dum=ListNode(0)
        prev=dum
        fin=str(fin)
        fin=fin[::-1]
        for i in fin:
            prev.next=ListNode(int(i))
            prev=prev.next
        return dum.next
            