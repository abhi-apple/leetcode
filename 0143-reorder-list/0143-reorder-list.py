# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        sl,fas=head,head.next
        while fas and fas.next:
            sl=sl.next
            fas=fas.next.next
            
        sec=sl.next
        sl.next=None
        prev=None
        
        while sec:
            fo=sec.next
            sec.next=prev
            prev=sec
            sec=fo
        #prev has the last node bcs the sec is null
        fir,sec=head,prev
        while sec:
            tmp1,tmp2=fir.next,sec.next
            fir.next=sec
            sec.next=tmp1
            fir=tmp1
            sec=tmp2
            
        
            
        
            
        