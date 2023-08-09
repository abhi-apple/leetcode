class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]+nums[j]==target:
                    cnt+=1
        return cnt