class Solution:
    def combinationSum(self, cd: List[int], tar: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur,tot):
            if tot==tar:
                res.append(cur.copy())
                return
            if i >=len(cd) or tot>tar:
                return
            cur.append(cd[i])
            dfs(i,cur,tot+cd[i])
            cur.pop()
            dfs(i+1,cur,tot)
        dfs(0,[],0)
        return res
        # def dfs(cd,target,start,path,res):
        #     if target<0:
        #         return 
        #     if target==0:
        #         res.append(path)
        #         return
        #     for i in range(start,len(cd)):
        #         dfs(cd,target-cd[i],i,path+[cd[i]],res)
        # res=[]
        # cd.sort()
        # dfs(cd,target,0,[],res)
        # return res