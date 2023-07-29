import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr=[]
        n=len(nums)
        for i,val in enumerate(nums):
            heapq.heappush(arr,(val,i))
        def rec(val,i):
            dic[i]=val
            if i>0:
                dic[i-1]=nums[i-1]
            if i<n-1:
                dic[i+1]=nums[i+1]
                
            
            
            
            
        dic={}
        cnt=0
        while len(dic)<n:
            num,ind=heapq.heappop(arr)
            if ind not in dic:
                cnt+=num
                rec(num,ind)
        # print(dic)
        return cnt