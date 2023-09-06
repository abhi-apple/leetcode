# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size=0
        cur=head
        while cur:
            cur=cur.next
            size+=1
        mainsize=size//k
        remsize=size%k
        eachlen=[mainsize]*k
        for i in range(remsize):
            eachlen[i]+=1
        cur=head
        res=[]
        for i in eachlen:
            partsize=i
            dumm=ListNode(0)
            new=dumm
            while partsize!=0:
                new.next=ListNode(cur.val)
                new=new.next
                cur=cur.next
                partsize-=1
            res.append(dumm.next)
                
            
        return res
        
            
        # mainsz=
        