class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortl(root):
            def findmid(node):
                if not node or not node.next:
                    return node
                
                fast , slow =node.next, node
                while fast and fast.next:
                    fast = fast.next.next
                    slow = slow.next
                return slow
            
            def merge(l1, l2):
                dumm = tail = ListNode()
                while l1 and l2:
                    if l1.val < l2.val:
                        tail.next = l1
                        l1 = l1.next
                    else:
                        tail.next = l2
                        l2 = l2.next
                    tail = tail.next
                tail.next = l1 or l2
                return dumm.next

            if not root or not root.next:
                return root
            
            left = root
            mid = findmid(root)
            right = mid.next
            mid.next = None

            left = sortl(left)
            right = sortl(right)
            return merge(left, right)

        return sortl(head)

