class Solution:
    def addDigits(self, num: int) -> int:
        nums=str(num)
        while len(nums)!=1:
            ans=0
            for i in nums:
                ans+=int(i)
            nums=str(ans)
        return int(nums)