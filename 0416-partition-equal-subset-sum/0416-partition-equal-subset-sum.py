class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ans=[]
        k=sum(nums)/2
        if not k.is_integer():
            return False
        n=len(nums)
        k=int(k)
        
        dp = [[False for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        if nums[0]<=k:
            dp[0][nums[0]]=True
        for i in range(1,n):
            for j in range(1,k+1):
                nk=dp[i-1][j]
                tk=False
                if nums[i]<=j:
                    tk=dp[i-1][j-nums[i]]
                dp[i][j]=nk or tk
        return dp[n-1][k]
        