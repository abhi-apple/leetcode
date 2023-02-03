#User function Template for python3

class Solution:
    def cutRod(self, pr, n):
        #code here
        
        dp=[[-1 for i in range(n+1)] for j in range(n)]
        def ans(ind,tar):
            if ind==0:
                return pr[0]*tar
            if dp[ind][tar]!=-1:
                return dp[ind][tar]
            nt=ans(ind-1,tar)
            tk=-1000
            rod=ind+1
            if rod<=tar:
                tk=pr[ind]+ans(ind,tar-rod)
            dp[ind][tar]=max(nt,tk)
            return max(nt,tk)
            
        return ans(n-1,n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends