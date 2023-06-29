class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=0
        for i in nums:
            ans=ans^i
        cnt=0
        while ans:
            if ans&1:
                break
            cnt+=1
            ans=ans>>1
        x1=0
        x2=0
        for i in nums:
            if i&(1<<cnt):
                x1=x1^i
            else:
                x2=x2^i
        return [x1,x2]
                