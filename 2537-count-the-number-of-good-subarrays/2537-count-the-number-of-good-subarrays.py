class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ct=defaultdict(int)
        ans=0
        pa=0
        l=0
        for x in nums:
            pa+=ct[x]
            ct[x]+=1
            while pa>=k:
                y=nums[l]
                ct[y]-=1
                pa-=ct[y]
                l+=1
            ans+=l
        return ans
        