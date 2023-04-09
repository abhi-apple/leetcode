class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n,k=len(colors),26
        indeg=[0 for i in range(n)]
        grap=[[] for i in range(n)]
        for u,v in edges:
            grap[u].append(v)
            indeg[v]+=1
        zerin=set(i for i in range(n) if indeg[i]==0)
        count=[[0]*k for i in range(n)]
        for i,c in enumerate(colors):
            count[i][ord(c)-ord('a')]+=1
            
        maxic,vis=0,0
        while zerin:
            u=zerin.pop()
            vis+=1
            for v in grap[u]:
                for i in range(k):
                    count[v][i]=max(count[v][i],count[u][i]+(ord(colors[v])-ord('a')==i))
                indeg[v]-=1
                if indeg[v]==0:
                    zerin.add(v)
            maxic=max(maxic,max(count[u]))
        return maxic if vis==n else -1