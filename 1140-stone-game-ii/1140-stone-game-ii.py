class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp={}
        def dfs(alic,i,m):
            if i==len(piles):
                return 0
            if (alic,i,m) in dp:
                return dp[(alic,i,m)]
            res=0 if alic else float("inf")
            tot=0
            for x in range(1,2*m+1):
                if i+x>len(piles):
                    break
                tot+=piles[i+x-1]
                if alic:
                    res=max(res,tot+dfs(not alic,i+x,max(m,x)))
                else:
                    res=min(res,dfs(not alic ,i+x,max(m,x)))
            dp[(alic,i,m)]=res
            return res
        return dfs(True,0,1)