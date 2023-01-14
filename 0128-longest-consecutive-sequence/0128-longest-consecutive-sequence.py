class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxi=0
        for i in nums:
            if i-1 not in nums:
                curn=i
                curl=1
                while curn+1 in nums:
                    curn+=1
                    curl+=1
                maxi=max(maxi,curl)
        return maxi