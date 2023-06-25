class Solution:
    def countRoutes(self, loc: List[int], start: int, fin: int, fuel: int) -> int:
        dp = {}
        n = len(loc)
        mod = 10**9 + 7
        
        def rec(i,  fu):
            if fu < 0:
                return 0
            cnt = 0
            if (i,  fu) in dp:
                return dp[(i, fu)]
            if i == fin:
                cnt+=1  # Continue the recursion with reduced fuel
            
            
            
            for j in range(n):
                if j != i :
                    cnt = (cnt + rec(j,  fu - abs(loc[i] - loc[j]))) % mod
            
            dp[(i, fu)] = cnt
            return cnt
        
        return rec(start, fuel) % mod

