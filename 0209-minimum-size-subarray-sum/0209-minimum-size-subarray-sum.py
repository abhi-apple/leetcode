class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        l = 0
        sums = 0
        min_len = float('inf')  # Initialize min_len to infinity
        
        while r < len(nums):
            sums += nums[r]  # Add nums[r] to the sum
            r += 1  # Increment r
            while sums >= target:  # If the sum is greater than or equal to the target, update min_len
                min_len = min(min_len, r - l)  # Update min_len
                sums -= nums[l]  # Subtract nums[l] from the sum
                l += 1  # Increment l
                
        if min_len == float('inf'):  # If min_len is still infinity, return 0
            return 0
        return min_len 
        # r=0
        # l=0
        # if sum(nums)<target:
        #     return 0
        # if sum(nums)==target:
        #     return 1
        # sums=0
        # while target>sums and r<len(nums):
        #     sums+=nums[r]
        #     r+=1
        # maxi=r-l
        # while r<len(nums):
        #     if sums>=target:
        #         maxi=min(maxi,r-l)
        #         l+=1
        #         sums-=nums[l]
        #     elif sums<target:
        #         r+=1
        #         if r<len(nums):
        #             sums+=nums[r]
        # return maxi
                