class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t=s[::-1]
        final=''
        def rec(st,ad):
            
            nonlocal final
            n=len(st)
            # print(st,ad,s[:n])
            if s[:n]==st:
                final=ad+s
                return True
            return False
                
                
        for i in range(len(t)):
            if rec(t[i:],t[:i]):
                return final
        return ''
                
            