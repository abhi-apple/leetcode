class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref=[0]
        for i in nums:
            if i & 1==1:
                pref.append(pref[-1]+1)
            else:
                pref.append(pref[-1])
        ans=0
        count = defaultdict(int)
        count[0]=1
        for i in range(len(nums)):
            cnt=pref[i+1]-k
            ans+=count[cnt]
            count[pref[i+1]]+=1
        return ans
        