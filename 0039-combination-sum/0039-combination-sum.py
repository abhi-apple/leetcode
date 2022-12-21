class Solution:
    def combinationSum(self, cd: List[int], target: int) -> List[List[int]]:
        def dfs(cd,target,start,path,res):
            if target<0:
                return 
            if target==0:
                res.append(path)
                return
            for i in range(start,len(cd)):
                dfs(cd,target-cd[i],i,path+[cd[i]],res)
        res=[]
        cd.sort()
        dfs(cd,target,0,[],res)
        return res