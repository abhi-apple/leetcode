#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        def fin(ind,we):
            if ind==0:
                if wt[0]<=we:
                    return val[0]
                else:
                    return 0
            if dp[ind][we]!=0:
                return dp[ind][we]
            nk=fin(ind-1,we)
            tk=-100
            if(wt[ind]<=we):
                tk=val[ind]+fin(ind-1,we-wt[ind])
            dp[ind][we]=max(nk,tk)
            return max(nk,tk)
        dp=[[0]*(W+1) for i in range(len(val))]
        
        
        return fin(len(val)-1,W)
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends