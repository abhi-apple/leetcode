#User function Template for python3

from typing import List
from collections import deque
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj={i:[] for i in range(n)}
        for i in edges:
            adj[i[0]].append((i[1],i[2]))
        st=[]
        vis=set()
        def top(node):
            vis.add(node)
            for v, _ in adj[node]:
                if v not in vis:
                    # print(v,'s')
                    top(v)
            st.append(node)
        for i in range(n):
            if i not in vis:
                top(i)
        dis=[]
        for i in range(n):
            dis.append(float('inf'))
        dis[0]=0
        while st:
            now=st.pop()
            for v,dic in adj[now]:
                if dis[now]+dic<dis[v]:
                    dis[v]=dis[now]+dic
        for i in range(len(dis)):
            if dis[i]==float('inf'):
                dis[i]=-1
        
        return dis
 
        # que=deque()
        # for i in range(n):
        #     if ind[i]==0:
        #         que.append(i)
        # top=[]
        # while que:
        #     fin=que.popleft()
            
        #     top.append(fin)
            
        #     for val in adj[fin]:
        #         ind[val[0]]-=1
        #         if ind[val[0]]==0:
        #             que.append(val[0])
        print(top)
        return [1]
        pass


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends