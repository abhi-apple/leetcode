class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pref=[]
        sums=0
        if len(nums)==k:
            return sum(nums)/k
        n=len(nums)
        for i in nums:
            sums+=i
            pref.append(sums)
        maxi=sum(nums[:k])
 
        for i in range(k,n):
            maxi=max(maxi,pref[i]-pref[i-k])
        return maxi/k
        # return 1.0