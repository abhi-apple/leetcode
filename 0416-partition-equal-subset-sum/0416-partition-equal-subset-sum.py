class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ans=[]
        main=sum(nums)/2
        if not main.is_integer():
            return False
        n=len(nums)
        
        dp=[[-1 for i in range(int(main)+1)] for j in range(n)]
        def fd(ind,k):
            if k==0:
                return True
            if ind==0:
                return nums[0]==k
            if (dp[ind][k]!=-1):
                return dp[ind][k]
            nt=fd(ind-1,k)
            tk=False
            if(nums[ind]<=k):
                tk=fd(ind-1,k-nums[ind])
            dp[ind][k]=nt or tk
            return nt or tk
        return fd(n-1,int(main))