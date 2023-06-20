class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
            
        n=len(s)
        def rec(i):
            if i==n:
                return 1
            if (i) in dp:
                return dp[i]
            ans=0
            if s[i]!='0':
                ans+=rec(i+1)
            if i+1<len(s) and (s[i]=='1' or(s[i]=='2' and s[i+1] in '0123456')):
                ans+=rec(i+2)
            dp[i]=ans
            return ans
        return rec(0)
        
        
        
#def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i]=='0':
        #         return 0
                
                
            