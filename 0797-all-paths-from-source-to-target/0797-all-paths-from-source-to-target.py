class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end=len(graph)-1
        que=[(0,[0])]
        paths=[]
        while que:
            node,path=que.pop(0)
            if node==end:
                paths.append(path)
            else:
                for i in graph[node]:
                    que.append((i,path+[i]))
        return paths