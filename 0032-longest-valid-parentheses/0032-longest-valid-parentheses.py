class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        maxi=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    maxi=max(maxi,i-st[-1])
        return maxi
#         def rec(i, op, cl):
#             nonlocal ans
#             if op == cl:
#                 ans = max(ans, op * 2)
#             if i == len(s):
#                 return
#             if s[i] == '(':
#                 rec(i + 1, op + 1, cl)
#             if s[i] == ')':
#                 if op > cl:
#                     rec(i + 1, op, cl + 1)
        
#         ans = 0
#         for i in range(len(s)):
#             if s[i] == '(':
#                 rec(i, 0, 0)
#         return ans
