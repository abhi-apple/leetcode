class Solution:
    def validateBinaryTreeNodes(self, n: int, lftch: List[int], rgtch: List[int]) -> bool:
        
        graph = defaultdict(list)
        
        indegre=[0]*n
        
        for node in range(n):
            left,right=lftch[node],rgtch[node]
            if left!=-1:
                graph[node].append(left)
                indegre[left]+=1
            if right!=-1:
                graph[node].append(right)
                indegre[right]+=1
        rootcand=[node for node in range(n) if indegre[node]==0]
        
        if len(rootcand)!=1:
            return False
        root=rootcand[0]
        
        que=[root]
        seen=set([root])
        
        while que:
            node=que.pop(0)
            if node in graph:
                for child in graph[node]:
                    if child in seen:
                        return False
                    seen.add(child)
                    que.append(child)
        return len(seen)==n
        