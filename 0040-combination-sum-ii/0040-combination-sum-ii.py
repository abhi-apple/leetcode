class Solution:
    def combinationSum2(self, cd: List[int], tar: int) -> List[List[int]]:
        cd.sort()
        res = set()
        
        def dfs(i, ar, t):
            if t == tar:
                res.add(tuple(ar))
                return
            for j in range(i,len(cd)):
                if j>i and cd[j]==cd[j-1]:
                    continue
                if t + cd[j] > tar:
                    break
                ar.append(cd[j])
                dfs(j+1, ar, t+cd[j])
                ar.pop()
        
        dfs(0, [], 0)
        return res
