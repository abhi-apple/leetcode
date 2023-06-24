class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(i==0 for i in nums):
            
            return '0'
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(reverse=True)  

        for _ in range(len(nums)):
            for i in range(1,len(nums)):
                if nums[i][0]==nums[i-1][0] and len(nums[i])!=len(nums[i-1]):
                    if int(nums[i]+nums[i-1])>int(nums[i-1]+nums[i]):
                        nums[i],nums[i-1]=nums[i-1],nums[i]
    
            
        
        return ''.join(nums)