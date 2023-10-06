class Solution:
    def __init__(self):
        self.dp = {}  # Initialize the memoization table

    def integerBreak(self, n: int) -> int:
        def rec(num):
            if num == 1:
                return 1
            if num in self.dp:
                return self.dp[num]
            maxi = 0
            for i in range(1, num):
                val = max(i * rec(num - i), i * (num - i))
                maxi = max(maxi, val)
            self.dp[num] = maxi
            return self.dp[num]

        return rec(n)
