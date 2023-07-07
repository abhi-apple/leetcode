class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        
        if k==0:
            return num
        num=list(num)
        for i in num:
            while st and st[-1]>i and k!=0:
                k-=1
                st.pop()
            st.append(i)
        while st and k!=0:
            st.pop()
            k-=1
            
        st=st[::-1]
        while st and st[-1]=='0':
            st.pop()
        st=st[::-1]
        if not st:
            return '0'
        return ''.join(st)
                