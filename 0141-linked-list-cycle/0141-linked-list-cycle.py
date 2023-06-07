# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ans=set()
        cur=head
        while cur:
            if cur.next in ans:
                return True
            ans.add(cur.next)
            cur=cur.next
        return False