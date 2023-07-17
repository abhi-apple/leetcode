# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(main):  
            cur=main
            prev1=None
            while cur:
                nxt=cur.next
                cur.next=prev1
                prev1=cur
                cur=nxt
            return prev1
        prev1=rev(l1)
        prev2=rev(l2)
        dummy=ListNode(0)
        res=dummy
        car=0
        while prev1 or prev2 or car:
            
            new=(prev1.val if prev1 else 0)+(prev2.val if prev2 else 0)+car
            car=new//10
            new=ListNode(new%10)
            res.next=new
            res=res.next
            prev1=prev1.next if prev1 else None
            prev2=prev2.next if prev2 else None
            
        return rev(dummy.next)
