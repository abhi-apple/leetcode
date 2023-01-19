class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            if nums[0] %k==0:
                return 1
            else:
                return 0
        pref=0
        fre={0:1}
        cnt=0
        for i in nums:
            pref=(pref+i)%k
            if pref in fre:
                cnt+=fre[pref]
                fre[pref]+=1
            else:
                fre[pref]=1
        return cnt
            
                