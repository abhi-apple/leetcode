class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st=[]
        res=[]
        def bck(ope,cld):
            if ope==cld==n:
                res.append(''.join(st))
                return
            if ope<n:
                st.append("(")
                bck(ope+1,cld)
                st.pop()
            if cld<ope:
                st.append(")")
                bck(ope,cld+1)
                st.pop()
        bck(0,0)
        return res
                