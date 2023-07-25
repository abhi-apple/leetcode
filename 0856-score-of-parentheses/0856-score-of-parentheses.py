class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s='('+s+')'
        def rec(st, ed):
            if st + 1 == ed:
                return 1
            else:
                ans = 0
                i=st+1
                while i<ed:
                    
                    if i in pair:
                        ans += rec(i, pair[i])
                        i=pair[i]+1
                    else:
                        ans+=0
                return ans * 2 if s[st] == '(' and s[ed] == ')' else ans

        n = len(s)
        pair = {}
        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                pair[st.pop()] = i

        return rec(0, n - 1)//2

# # Test case
# sol = Solution()
# print(sol.scoreOfParentheses("(()(()))"))  # Output: 6
