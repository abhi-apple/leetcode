class Solution:
    def kConcatenationMaxSum(self, array: List[int], k: int) -> int:
        sums=sum(array)
        mod=10**9 +7
        def kadane(nums):
            for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
            return max(max(nums), 0)
        if k==1:
            return kadane(array)%mod
        if sums>0:
            return (kadane(array+array)+ (k-2)*sums)%mod
        else:
            return kadane(array+array)%mod