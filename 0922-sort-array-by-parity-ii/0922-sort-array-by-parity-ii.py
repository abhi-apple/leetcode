class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev=[]
        od=[]
        for i in range(len(nums)):
            if nums[i] & 1==1:
                od.append(nums[i])
            else:
                ev.append(nums[i])
        ans=[]
        for i in range(len(nums)):
            if i & 1==1:
                ans.append(od.pop())
            else:
                ans.append(ev.pop())
        return ans