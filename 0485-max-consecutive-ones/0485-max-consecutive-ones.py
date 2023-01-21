class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        main=0
        for i in nums:
            if i==1:
                maxi+=1
            else:
                maxi=0
            main=max(main,maxi)
        return main
                