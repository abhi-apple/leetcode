class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1=0
        p2=len(s)-1
        while p1<=p2:
            if s[p1]!=s[p2]:
                st1=s[:p1]+s[p1+1:]
                st2=s[:p2]+s[p2+1:]
                return st1==st1[::-1] or st2==st2[::-1]
            p1+=1
            p2-=1
        return True
