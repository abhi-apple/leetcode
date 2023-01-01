class Solution:
    def simplifyPath(self, path: str) -> str:
        dic=path.split('/')
        st=[]
        for i in dic:
            if i=='':
                continue
            elif i=='..':
                if st:
                    st.pop()
            elif i!='.':
                st.append(i)
        res='/'+'/'.join(st)
        return res