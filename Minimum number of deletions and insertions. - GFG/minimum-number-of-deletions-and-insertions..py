#User function Template for python3
class Solution:
	def minOperations(self, s, r):
        n=len(s)
        m=len(r)
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==r[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n+m- 2*dp[n][m]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends