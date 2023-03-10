class Solution:
    def maxProfit(self, p: List[int]) -> int:
        prof=0
        mini=p[0]
        for i in range(1,len(p)):
            prof=max(prof,p[i]-mini)
            mini=min(p[i],mini)
        return prof