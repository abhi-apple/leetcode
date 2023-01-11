class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1] == 0:
                    return True
            return False
        prefix_sum = [0] * (len(nums) + 1)
        seen = {0: -1}
        for i in range(len(nums)):
            prefix_sum[i + 1] = (prefix_sum[i] + nums[i]) % k
            if prefix_sum[i + 1] in seen:
                if i - seen[prefix_sum[i + 1]] > 1:
                    return True
            else:
                seen[prefix_sum[i + 1]] = i
        return False