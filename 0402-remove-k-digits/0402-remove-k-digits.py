class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = list(num)
        st = []
        for i in ans:
            while st and st[-1] > i and k > 0:
                st.pop()
                k -= 1
            st.append(i)
        st = st[:len(st)-k]
        while st and st[0] == "0":
            st.pop(0)
        # Return "0" if k is non-zero
        return "".join(st) or "0"
