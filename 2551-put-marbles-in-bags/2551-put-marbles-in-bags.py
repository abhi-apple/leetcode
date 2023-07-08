class Solution:
    def putMarbles(self, we: List[int], k: int) -> int:
        ans=[]
        for i in range(len(we)-1):
            ans.append(we[i+1]+we[i])
        ans.sort()
        n=len(we)
        sums=0
        for i in range(k-1):
            sums+=(ans[n-2-i]-ans[i])
        return sums