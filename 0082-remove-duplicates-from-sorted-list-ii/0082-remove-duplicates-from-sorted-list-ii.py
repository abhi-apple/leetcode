# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans={}
        ab=head
        while head:
            if head.val in ans:
                ans[head.val]+=1
            else:
                ans[head.val]=1
            head=head.next
        res=set()
        for i in ans:
            if ans[i]>1:
                res.add(i)
        
            
        head=ab
        dum=ListNode(101)
        dum.next=head
        prev,cur=dum,head
        while cur:
            nxt=cur.next
            if cur.val in res:
                prev.next=nxt
            else:
                prev=cur
            cur=nxt
        return dum.next
            