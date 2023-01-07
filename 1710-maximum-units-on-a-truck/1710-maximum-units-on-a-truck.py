class Solution:
    def maximumUnits(self, bxt: List[List[int]], ts: int) -> int:
        bxt.sort(key=lambda a:-a[1])
        ans=0
        for i in bxt:
            if ts<0 : break
            ans+=min(ts,i[0])*i[1]
            ts-=i[0]
        return ans
