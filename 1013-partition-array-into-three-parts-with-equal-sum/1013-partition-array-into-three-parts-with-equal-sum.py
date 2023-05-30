class Solution:
    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        sums=sum(nums)
        if sums%3!=0:
            return False
        sums=sums//3
        cnt=0
        val=0
        for i in range(len(nums)):
            val+=nums[i]
            if val==sums:
                cnt+=1
                val=0
        return True if cnt>=3 else False