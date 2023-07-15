class Solution:
    def canFinish(self, numc: int, pre: List[List[int]]) -> bool:
        adj = [[] for _ in range(numc)]
        indegree = [0] * numc

        for it in pre:
            adj[it[1]].append(it[0])
            indegree[it[0]] += 1
        stack=deque()
        for i in range(numc):
            if indegree[i]==0:
                
                stack.append(i)
        cnt=0
        while stack:
            node=stack.popleft()
            cnt+=1
            for var in adj[node]:
                indegree[var]-=1
                if indegree[var]==0:
                    stack.append(var)
        if cnt==numc:
            return True
        return False