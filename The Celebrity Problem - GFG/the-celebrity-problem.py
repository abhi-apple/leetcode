#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, m, n):
        # code here 
        dp={i:[False,0] for i in range(n)}
        
        for i in range(n):
            for j in range(n):
                if m[i][j]==1:
                    dp[j][1]+=1
                    dp[i][0]=True
        for k in dp:
            if dp[k][0]==False:
                if dp[k][1]==n-1:
                    return k
        return -1
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends