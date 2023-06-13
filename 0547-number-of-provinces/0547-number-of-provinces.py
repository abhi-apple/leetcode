class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        dic={}
        vis=[]
        for i in range(len(isc)):
            dic[i]=[]
            for k in range(len(isc[i])):
                if i!=k:
                    if isc[i][k]==1:
                        dic[i].append(k)
        cnt=0
        def dfs(node):
            vis.append(node)
            for i in dic[node]:
                if i not in vis:
                    dfs(i)
                    
        for i in dic:
            if i not in vis:
                dfs(i)
                cnt+=1
        return cnt
            
                
            