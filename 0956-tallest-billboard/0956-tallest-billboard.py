class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        ans={}
        
        def rec(i,diff):
            if (i,diff) in ans:
                return ans[(i,diff)]
            if i>=len(rods):
                if diff:
                    return -float('inf')
                return 0
            long=rec(i+1,diff+rods[i])
            skip=rec(i+1,diff)
            short=rec(i+1,diff-rods[i])+rods[i]
            ans[(i,diff)]=max(long,skip,short)
            return ans[(i,diff)]
        return rec(0,0)