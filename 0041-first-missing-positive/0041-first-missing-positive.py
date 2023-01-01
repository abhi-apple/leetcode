class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=0
        for num in nums:
            if num>0:
                k+=1
        A=[0]*k
        for num in nums:
            if num>0 and num <= k:
                A[num-1]=1
        for i in range(k):
            if A[i]==0:
                return i+1
        return k+1