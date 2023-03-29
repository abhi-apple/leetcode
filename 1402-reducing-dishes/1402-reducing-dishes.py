class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        pfs=0
        curs=0
        maxs=0
        for num in sorted(satisfaction,reverse=True):
            print(num)
            pfs+=num
            curs+=pfs
            maxs=max(maxs,curs)
            
        return maxs