# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res
#         if not head.next:
#             return [0]
#         dum=ListNode(0,head)
#         res=[]
        
#         prev=dum
#         cur=dum.next.next
#         while head:
#             ad=False
#             while cur:
#                 if head.val<cur.val:
#                     res.append(cur.val)
#                     ad=True
#                     break
#                 cur=cur.next
#             if ad==False:
#                 res.append(0)
#             head=head.next
#             cur=head
#         return res
                
            