class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Replace negative numbers and zero with n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # Mark the presence of each number in the array
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num-1] = -abs(nums[num-1])

        # Return the first index with a positive value
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # If no positive values were found, return n+1
        return n + 1

        # if len(nums)==1:
        #     if nums[0]==1:
        #         return 2
        #     else:
        #         return 1
        # maxi=max(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         return i
        # return maxi+1