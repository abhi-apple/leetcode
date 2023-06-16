

from typing import List

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for it in pre:
            adj[it[1]].append(it[0])
            indegree[it[0]] += 1
        que=deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
                    
        top=0
        while que:
            node=que.popleft()
            top+=1
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it]==0:
                    que.append(it)
        print(top)
        if top==numCourses:
            return True
        return False
      