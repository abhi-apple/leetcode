class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts=[0]+cuts
        cuts.append(n)
        cuts.sort()
        dp={}
        def rec(i,j):
       
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            mini=float('inf')
            for k in range(i,j+1):
                val=(cuts[j+1]-cuts[i-1]) + rec(i,k-1)+rec(k+1,j)
                mini=min(val,mini)
            dp[(i,j)]=mini
            return dp[(i,j)]
        
        return rec(1,len(cuts)-2)