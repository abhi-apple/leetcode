class Solution:
    def removeDigit(self, nums: str, dig: str) -> str:
        maxi=0
        for i in range(len(nums)):
            if nums[i]==dig:
                ans=nums[:i]+nums[i+1:]
                maxi=max(maxi,int(ans))
        return str(maxi)