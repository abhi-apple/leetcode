class Solution:
    
    def numTilings(self, n: int) -> int:
        MOD=10**9+7
        if n==0 or n==1:
            return 1
        f=[0]*(n+1)
        f[0]=1
        f[1]=1
        for i in range(2,n+1):
            f[i]=2*f[i-1] +f[i-3]
        return f[n]%MOD