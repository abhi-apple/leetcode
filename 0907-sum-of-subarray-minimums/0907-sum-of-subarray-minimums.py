class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        lft=[1]*n
        dec=[(arr[0],1)]
        for i in range(1,n):
            while dec and arr[i]<=dec[-1][0]:
                lft[i]+=dec.pop()[1]
            dec.append((arr[i],lft[i]))
        rgt=[1]*n
        dec=[(arr[-1],1)]
        for i in range(n-2,-1,-1):
            while dec and arr[i]<dec[-1][0]:
                rgt[i]+=dec.pop()[1]
            dec.append((arr[i],rgt[i]))
        ans=0
        for i in range(n):
            ans=(ans+(arr[i]*lft[i]*rgt[i]))%(10**9 +7)
        return ans
