# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            p=i
            while p is not None:
                arr.append(p.val)
                p=p.next
        arr.sort()
        link=ListNode()
        p=link
        for i in arr:
            p.next=ListNode(i)
            p=p.next
        return link.next