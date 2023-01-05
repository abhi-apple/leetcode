class Solution:
    def findMinArrowShots(self, pts: List[List[int]]) -> int:
        pts.sort(key=lambda p:p[1])
        ans,arr=0,0
        for [st,end] in pts:
            if ans==0 or st>arr:
                ans,arr=ans+1,end
        return ans