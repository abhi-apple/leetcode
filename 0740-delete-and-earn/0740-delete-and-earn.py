class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        nums=sorted(list(set(nums)))
        ern1=0
        ern2=0
        for i in range(len(nums)):
            cur=nums[i]*cnt[nums[i]]
            if i>0 and nums[i]==nums[i-1]+1:
                ern1,ern2=max(cur+ern2,ern1),ern1
                
                # tmp=ern1
                # ern1=max(cur,ern2)
                # ern2=tmp
            else:
                ern1,ern2=cur+ern1,ern1
        return max(ern1,ern2)