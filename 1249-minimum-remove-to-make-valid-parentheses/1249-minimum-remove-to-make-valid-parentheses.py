class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                # print(i)
                if st and s[st[-1]]=='(':
                    st.pop()
                else:
                    st.append(i)
        s=list(s)
        # print(st)
        for i in st:
            s[i]=''
        return ''.join(s)
    
    
    
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         st=[]
#         sp=list(s)
#         for i in range(len(s)):
#             if s[i]=='(':
#                 st.append(i)
#             elif s[i]==')':
#                 if st:
#                     st.pop()
#                 else:
#                     sp[i]=''
#         print(st,sp)
#         for i in st:
#             sp[i]=''
#         return ''.join(sp)