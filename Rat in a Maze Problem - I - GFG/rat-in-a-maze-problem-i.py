#User function Template for python3

class Solution:
    def solve(self, i, j, a, n, ans, move, vis, di, dj):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return

        dir = "DLRU"
        for ind in range(4):
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if (nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1):
                vis[i][j] = 1
                self.solve(nexti, nextj, a, n, ans, move + dir[ind], vis, di, dj)
                vis[i][j] = 0

    def findPath(self, m, n):
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]

        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", vis, di, dj)
        
        return ans

# class Solution:
#     def solve(self,i,j,mat,n,ans,st,vis,di,dj):
#         if i==n-1 and j==n-1:
#             ans.append(st.copy())
            
#             return
#         dis="DLRU"
#         for iq in range(4):
#             ni=i+di[iq]
#             nj=j+dj[iq]
        
#             if(ni>=0 and nj>=0 and ni<n and nj<n and vis[ni][nj]!=1 and mat[ni][nj]==1):
#                 vis[i][j]=1
#                 self.solve(ni,nj,mat,n,ans,st+dis[iq],vis,di,dj)
#                 vis[i][j]=0
#     def findPath(self, m, n):
#         # code here

#         ans=[]
#         vis=[[0]*n for _ in range(n)]
#         di=[1,0,0,-1]
#         dj=[0,-1,1,0]
        
#         if(m[0][0]==1):
#             self.solve(0,0,m,n,ans,"",vis,di,dj)
#         return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends