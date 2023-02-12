class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        gp=defaultdict(list)
        for x,y in roads:
            gp[x].append(y)
            gp[y].append(x)
        self.ans=0
        def dfs(i,prev,pep=1):
            for x in gp[i]:
                if x==prev: continue
                pep+=dfs(x,i)
            self.ans+=(int(ceil(pep/seats)) if i else 0)
            return pep
        dfs(0,0)
        return self.ans