class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nei = defaultdict(list)
        for source, dest, price in flights:
            nei[source].append([dest, price])
        q = [[0,src,0]]
        dis=[10**9 for i in range(n)]
        dis[src]=0
        while(q):
            stp,nd,cst=q.pop(0)
            if stp>k:
                continue
            for i in nei[nd]:
                nod=i[0]
                cos=i[1]
                
                if cst+cos<dis[nod] and stp<=k:
                    dis[nod]=cst+cos
                    q.append([stp+1,nod,cst+cos])
        
        if (dis[dst]==10**9):
            return -1
        return dis[dst]