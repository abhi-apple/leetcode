class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def isbi(adj,n,i,col):
            que=[]
            que.append(i)
            col[i]=1
            while que:
                curr=que.pop(0)
                for i in adj[curr]:
                    if col[i]==col[curr]:
                        return False
                    if col[i]==-1:
                        col[i]=1-col[curr]
                        que.append(i)
            return True
        adl=defaultdict(list)
        for a,b in dislikes:
            adl[a].append(b)
            adl[b].append(a)
        col=[-1]*(n+1)
        for i in range(1,n+1):
            if col[i]==-1:
                if not isbi(adl,n,i,col):
                    return False
        return True
