class Solution:
    def longestPalindrome(self, s: str) -> str:
        lgt=0
        stl=''
        def rec(l,r):
            nonlocal lgt,stl
            while 0<=l and r<len(s) and s[l]==s[r]:
                if r-l+1>lgt:
                    stl=s[l:r+1]
                    lgt=r-l+1
                    
                l-=1
                r+=1
        for i in range(len(s)):
            rec(i,i)
            rec(i,i+1)
        return stl
            