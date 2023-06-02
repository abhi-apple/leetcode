class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj =collections.defaultdict(list)
        ans=0
        
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1=bombs[i]
                x2,y2,r2=bombs[j]
                d=sqrt((x1-x2)**2 + (y1-y2)**2)
                if d<=r1:
                    adj[i].append(j)
                if d<=r2:
                    adj[j].append(i)
        def dfs(i):
            if i in vis:
                return 0
            vis.add(i)
            res=0
            for ni in adj[i]:
                dfs(ni)
            return len(vis)
            
            
        for i in range(len(bombs)):
            vis=set()
            ans=max(dfs(i),ans)
        return ans
                