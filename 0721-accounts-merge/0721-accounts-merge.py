class Solution:
    def accountsMerge(self, acc: List[List[str]]) -> List[List[str]]:
        size = [1] * len(acc)
        par = [i for i in range(len(acc))]
        
        def find(i):
            if par[i] == i:
                return i
            par[i] = find(par[i])
            return par[i]
        
        def union(i, j):
            pi = find(i)
            pj = find(j)
            if size[pi] > size[pj]:
                par[pj] = pi
                size[pi] += size[pj]
            else:
                par[pi] = pj
                size[pj] += size[pi]
        
        dic = {}
        for i in range(len(acc)):
            for j in range(1, len(acc[i])):
                if acc[i][j] not in dic:
                    dic[acc[i][j]] = i
                else:
                    union(i, dic[acc[i][j]])
        
        fin = [[] for _ in range(len(acc))]
        for res in dic:
            mainpar = find(dic[res])
            fin[mainpar].append(res)
        
        res=[]
        for i in range(len(acc)):
            
            if fin[i]!=[]:
                now=[acc[i][0]]
                now.extend(sorted(fin[i]))
                res.append(now)
                
        return res
