# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, nums: List[Optional[ListNode]]) -> Optional[ListNode]:
        fin=[]
        for i in nums:
            while i:
                fin.append(i.val)
                i=i.next
        fin.sort()
        dum=ListNode(0)
        prev=dum
        for i in fin:
            prev.next=ListNode(i)
            prev=prev.next
        return dum.next
            
            
                