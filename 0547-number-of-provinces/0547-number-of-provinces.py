class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        n=len(isc)
        par=[i for i in range(n)]
        size=[1 for _ in range(n)]
        
        def find(i):
            if par[i]==i:
                return i
            par[i]=find(par[i])
            return par[i]
        def union(i,j):
            pi=find(i)
            pj=find(j)
            if pi!=pj:
                if size[pi]<size[pj]:
                    par[pi]=pj
                    size[pj]+=size[pi]
                else:
                    par[pj]=pi
                    size[pi]+=size[pj]
        for i in range(n):
            for j in range(n):
                if i!=j and isc[i][j]:
                    union(i,j)
        cnt=0
        for i in range(n):
            if par[i]==i:
                cnt+=1
                
        return cnt