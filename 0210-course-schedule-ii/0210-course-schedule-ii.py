class Solution:
    def findOrder(self, nums: int, p: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(nums)}
        ind = [0] * nums
        for i in p:
            adj[i[1]].append(i[0])
            ind[i[0]]+=1
        que=deque()
        for i in range(nums):
            if ind[i]==0:
                que.append(i)
        top=[]
        while que:
            var=que.popleft()
            top.append(var)
            for i in adj[var]:
                ind[i]-=1
                if ind[i]==0:
                    que.append(i)
        if len(top)==nums:
            return top
        return []
            