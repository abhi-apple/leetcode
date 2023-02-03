#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s, t, n, m):
        # code here
        prev=[0 for i in range(m+1)]
        cur=[0 for i in range(m+1)]
        
        ans=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    cur[j]=1+prev[j-1]
                    ans=max(ans,cur[j])
                else:
                    cur[j]=0
            prev=cur[:]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends