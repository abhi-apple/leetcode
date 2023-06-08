class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            for num in nums:
                
                if num not in arr:
                    backtrack(arr+[num])
                    # arr.append(num)
                    # backtrack(arr)
                    # arr.pop()

        ans = []
        backtrack([])
        return ans