class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        ans=1
        for num in arr:
            if num-difference in dp:
                dp[num]=dp[num-difference]+1
            else:
                dp[num]=1
            ans=max(ans,dp[num])
        return ans