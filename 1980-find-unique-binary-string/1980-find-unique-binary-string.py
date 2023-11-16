class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        nums=set(nums)
        ans=''
        def rec(strs):
            nonlocal ans
            if len(strs)==n:
                if strs not in nums:
                    ans=strs
                return 
            addone=rec(strs+'1')
            addzero=rec(strs+'0')
            return 
        rec('')
        return ans
        