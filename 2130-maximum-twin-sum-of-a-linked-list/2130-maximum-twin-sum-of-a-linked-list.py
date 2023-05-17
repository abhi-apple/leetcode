# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        node=head
        while node:
            arr.append(node.val)
            node=node.next
        i=0
        j=len(arr)-1
        maxi=0
        while i<j:
            maxi=max(maxi,arr[i]+arr[j])
            i+=1
            j-=1
        return maxi
            