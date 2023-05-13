class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans = 0
        mod = 10**9 + 7  # corrected the value of mod

        def rec(sz, dp):
            if sz == 0:
                return 1
            if sz < 0:
                return 0
            if dp[sz] != -1:
                return dp[sz]

            # Recursively calculate the number of good strings of length sz
            sm = (rec(sz - zero, dp) + rec(sz - one, dp)) % mod
            dp[sz] = sm
            return sm

        dp = [-1] * (high + 1)
        for i in range(low, high + 1):
            ans = ((ans % mod) + (rec(i, dp) % mod)) % mod

        return ans % mod
