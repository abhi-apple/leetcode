class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        st = []
        for i, n in enumerate(mat):
            st.append([sum(n), i])
        st.sort()
        return [k for j, k in st[0:k]]