class Solution:
    def numOfMinutes(self, n: int, he: int, man: List[int], inf: List[int]) -> int:
        dic={}
        for i in range(n):
            if man[i] in dic:
                dic[man[i]].append(i)
            else:
                dic[man[i]]=[]
                dic[man[i]].append(i)
        maxi=0
        def dfs():
            nonlocal maxi
            deq=deque()
            deq.append([-1,0])
            while deq:
                node,cnt=deq.popleft()
                if node in dic:
                    
                    for i in dic[node]:
                        deq.append([i,cnt+inf[i]])
                        maxi=max(maxi,cnt+inf[i])
            return maxi
            
            
        return dfs()
 