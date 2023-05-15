# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans=[]
        dum=head
        k=k-1
        while dum:
            ans.append(dum.val)
            dum=dum.next
        frn=ans[k]
        ed=ans[-(k+1)]
        print(frn,ed)
        for i in range(len(ans)):
            if i==k:
                ans[i]=ed
            if i==len(ans)-(k+1):
                ans[i]=frn
            
        new_head = ListNode(ans[0])
        curr_node = new_head
        for val in ans[1:]:
            new_node = ListNode(val)
            curr_node.next = new_node
            curr_node = new_node
        return new_head