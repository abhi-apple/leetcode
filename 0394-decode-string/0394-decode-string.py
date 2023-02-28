class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        if s.isdigit():
            return ''
        for i in range(len(s)):
            if s[i]!=']':
                st.append(s[i])
            else:
                sbsr=''
                while st[-1]!='[':
                    sbsr=st.pop()+sbsr
                st.pop()
                k=''
                while st and st[-1].isdigit():
                    k=st.pop()+k
                st.append(int(k)*sbsr)
        return ''.join(st)
