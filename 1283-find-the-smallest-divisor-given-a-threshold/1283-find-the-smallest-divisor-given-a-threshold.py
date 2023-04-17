class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calculate_sum(divisor):
            total_sum = 0
            for num in nums:
                total_sum += math.ceil(num/divisor)
            return total_sum
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            total_sum = calculate_sum(mid)
            if total_sum > threshold:
                left = mid + 1
            else:
                right = mid
        return left
