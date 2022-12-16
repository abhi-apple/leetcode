class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        cnt=0
        for i in nums:
            if freq[i]==1:
                cnt+=i
        return cnt