class Solution:
    def combinationSum2(self, cd: List[int], tar: int) -> List[List[int]]:
        
        def dfs(i,cd,t,ls,cur):
            if tar==t:
                ls.append(cur.copy())
                return
            for k in range(i,len(cd)):
                if k>i and cd[k]==cd[k-1]:
                    continue
                if t+cd[k]>tar:
                    break
                cur.append(cd[k])
                dfs(k+1,cd,t+cd[k],ls,cur)
                cur.pop()
        ls=[]
        cd.sort()
        dfs(0,cd,0,ls,[])
        return ls
        