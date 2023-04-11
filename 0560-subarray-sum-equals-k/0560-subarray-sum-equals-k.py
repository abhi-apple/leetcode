class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        d={0:1}
        p=0
        for i in nums:
            p=p+i
            if p-k in d:
                cnt+=d[p-k]
            if p not in d:
                d[p]=1
            else:
                d[p]+=1
        return cnt
                