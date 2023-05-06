class Solution:
    def combinationSum(self, cd: List[int], tar: int) -> List[List[int]]:
        res=[]
        def dfs(i,a,t):
            if tar==t:
                res.append(a.copy())
                return
            if i>=len(cd) or t>tar:
                return 
            a.append(cd[i])
            dfs(i,a,t+cd[i])
            a.pop()
            dfs(i+1,a,t)
            
            
            
        dfs(0,[],0)
        return res