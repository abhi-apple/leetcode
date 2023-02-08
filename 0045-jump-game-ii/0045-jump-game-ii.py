class Solution:
    def jump(self, nums: List[int]) -> int:
        cur,ne=0,0
        ret=0
        for i in range(len(nums)-1):
            cur=max(cur,i+nums[i])
            if i==ne:
                ret+=1
                ne=cur
        return ret