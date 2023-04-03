class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        dic = {}
        
        def dfs(ind, maps, visi):
            visi[ind] = 1
            if ind in maps:
                for i in maps[ind]:
                    if not visi[i]:
                        dfs(i, maps, visi)
            
        for i in range(len(isc)):
            for j in range(len(isc[0])):
                if isc[i][j] == 1 and i != j:
                    if i in dic:
                        dic[i].append(j)
                    else:
                        dic[i] = [j]
                    if j in dic:
                        dic[j].append(i)
                    else:
                        dic[j] = [i]
        vis = [0 for i in range(len(isc))]
        cnt = 0
        for i in range(len(isc)):
            if not vis[i]:
                cnt += 1
                dfs(i, dic, vis)
        return cnt
