# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, ha: ListNode, hb: ListNode) -> Optional[ListNode]:
        nodes = set()
        while ha:
            nodes.add(ha)
            ha = ha.next
        while hb:
            if hb in nodes:
                
                return hb
            hb = hb.next
        
        return None
        