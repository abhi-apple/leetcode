class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=0
        cnt=0
        res=[]
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                res.append(cnt)
                cnt=0
        res.append(cnt)
        if len(res)==1:
            return res[-1]-1
        maxi=0
        cur=res[0]
        for i in res[1:]:
            maxi=max(maxi,cur+i)
            cur=i
        return maxi
            
