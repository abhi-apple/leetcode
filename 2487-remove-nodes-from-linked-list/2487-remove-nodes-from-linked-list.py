class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        def rev(val):
            prev = None
            cur = val
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        new_reversed = rev(head)
        # print(new_reversed)
        cur = new_reversed
        while cur:
            if not st:
                st.append(cur.val)
            else:
                st.append(max(cur.val, st[-1]))
            cur = cur.next
        st = st[::-1]
        dummy = ListNode(0)
        lst = dummy
        # print(new_reversed)
        cur = rev(new_reversed)
        i = 0
        while cur:
            if cur.val == st[i]:
                lst.next = cur
                lst = lst.next
            i += 1
            cur = cur.next
        lst.next = None  # Set the next of the last node to None to terminate the list
        return dummy.next
