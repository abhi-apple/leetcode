class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        total_sum = sum(nums)

        left_sum = 0
        right_sum = total_sum

        for i in range(n):
            result[i] = i * nums[i] - left_sum + right_sum - (n - i) * nums[i]
            left_sum += nums[i]
            right_sum -= nums[i]

        return result
