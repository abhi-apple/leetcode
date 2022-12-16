class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans=[0]*2
        C=Counter(nums)
        for i in C.values():
            ans[0]+=(i//2)
            ans[1]+=(i%2)
        return ans
            