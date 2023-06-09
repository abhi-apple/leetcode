class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}  # Memoization dictionary to store calculated results
        
        def rec(i):
            if i >= len(nums) - 1:
                return 0  # Already at the last index, no need to jump
            
            if i in dp:
                return dp[i]
            
            res = float('inf')  # Initialize result with infinity
            
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    res = min(res, 1 + rec(i + j))  # Calculate minimum jumps recursively
            
            dp[i] = res  # Store the result in memoization dictionary
            return dp[i]
        
        return rec(0)
