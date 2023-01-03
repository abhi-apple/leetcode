class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        sp=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                if len(st)!=0:
                    st.pop()
                else:
                    sp[i]=''
        print(st,sp)
        for i in st:
            sp[i]=''
        return ''.join(sp)