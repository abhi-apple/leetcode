class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        max_sum = float('-inf')
        curr_max = 0
        min_sum = float('inf')
        curr_min = 0
        
        for num in nums:
            total_sum += num
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
        
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum
                
            