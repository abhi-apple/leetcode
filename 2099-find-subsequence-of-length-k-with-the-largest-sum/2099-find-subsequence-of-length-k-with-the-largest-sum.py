class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans=nums.copy()
        ans.sort(reverse=True)
        ans=ans[:k]
        res=[]
        for i in nums:
            if i in ans:
                res.append(i)
                ans.remove(i)
        return res