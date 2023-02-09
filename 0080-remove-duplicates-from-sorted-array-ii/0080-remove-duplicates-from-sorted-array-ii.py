class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic={}
        cnt=0
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
            if dic[nums[i]]>2:
                nums[i]=10001
                cnt+=1
        nums.sort()
        return len(nums)-cnt
        
                
        