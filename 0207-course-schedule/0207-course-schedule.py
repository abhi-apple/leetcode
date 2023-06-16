

from typing import List

class Solution:
    def canFinish(self, numc: int, pre: List[List[int]]) -> bool:
        adj={}
        for k in pre:
            i,j=k
            if i in adj:
                adj[i].append(j)
            else:
                adj[i]=[j]
        for i in range(numc):
            if i not in adj:
                adj[i]=[]
        print(adj)
        def dfs(node):
            vis.add(node)
            if adj[node]!=[]:
                st.add(node)
            if adj[node]==[]:
                return True
            
            for neighbor in adj[node]:
                if neighbor in st:
                    return False
                if neighbor not in vis:
                    if not dfs(neighbor):
                        return False
                    
            st.remove(node)
            adj[node]=[]
            return True
        vis=set()
        for k in adj:
            if adj[k]!=[]:
                
                st=set()
                if k not in vis:
                    if not dfs(k):
                        return False
        
        return True
                    
      