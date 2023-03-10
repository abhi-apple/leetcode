# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head
        

    def getRandom(self) -> int:
        ans=self.head
        cnt=0
        while ans and ans.next:
            cnt+=1
            ans=ans.next
        ans=self.head
        num = random.randint(0,cnt)
   
        while num!=0:
            ans=ans.next
            num-=1
        return ans.val
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()