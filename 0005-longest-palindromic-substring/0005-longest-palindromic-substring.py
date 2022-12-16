class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n=len(s)
        # longstr=""
        # for i in range(n,0,-1):
        #     for j in range(n-i+1):
        #         subst=s[j:j+i]
        #         if subst==subst[::-1] and len(subst)>len(longstr):
        #             longstr=subst
        # return longstr
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""
        for i in range(len(s)):
            # Check palindromes with odd lengths
            palindrome = expandAroundCenter(i, i)
            if len(palindrome) > len(result):
                result = palindrome
            # Check palindromes with even lengths
            palindrome = expandAroundCenter(i, i+1)
            if len(palindrome) > len(result):
                result = palindrome
        return result