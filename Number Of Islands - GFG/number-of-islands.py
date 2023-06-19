#User function Template for python3

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        n=rows*cols
        par=[i for i in range(n)]
        size=[1]*n
        def find(node):
            if par[node]==node:
                return node
            par[node]=find(par[node])
            return par[node]
        def union(i,j):
            pi=find(i)
            pj=find(j)
            if size[pi]<size[pj]:
                par[pi]=pj
                size[pj]+=size[pi]
            else:
                par[pj]=pi
                size[pi]+=size[pj]
        vis=set()
        cnt=0
        ans=[]
        for i,j in operators:
            if (i,j) in vis:
                ans.append(cnt)
                continue
            vis.add((i,j))
            cnt+=1
            dire=[(0,-1),(-1,0),(1,0),(0,1)]
            for d in dire:
                ix,jx=i+d[0],j+d[1]
                if 0<=ix<rows and 0<=jx<cols :
                    if (ix,jx) in vis:
                        nd=i*cols +j
                        adj=ix*cols+jx
                        if (find(nd)!=find(adj)):
                            cnt-=1
                            union(nd,adj)
            ans.append(cnt)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends