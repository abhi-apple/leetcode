class Solution:
    def stoneGameIII(self, st: List[int]) -> str:
        dic={}
        def dfs(i):
            if i==len(st):
                return 0
            if i in dic:
                return dic[i]
            res=float("-inf")
            for j in range(i,min(i+3,len(st))):
                res=max(res,sum(st[i:j+1])-dfs(j+1))
            dic[i]=res
            return res
        return "Alice" if dfs(0)>0 else("Bob" if dfs(0)<0 else "Tie")