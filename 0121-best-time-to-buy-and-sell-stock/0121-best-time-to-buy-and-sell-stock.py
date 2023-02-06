class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mini=p[0]
        prof=0
        
        for i in range(1,len(p)):
            cos=p[i]-mini
            prof=max(prof,cos)
            mini=min(mini,p[i])
        return prof
            