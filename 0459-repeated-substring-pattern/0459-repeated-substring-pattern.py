class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n=len(s)
        if n==1:
            return False
        new=''
        for i in range((n+1)//2):
            new+=s[i]
            if n%len(new)==0:
                if new*(n//len(new))==s:
                    return True
        return False