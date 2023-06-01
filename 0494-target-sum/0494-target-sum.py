class Solution:
    def findTargetSumWays(self, nums: List[int], t: int) -> int:
        dp = {}

        def rec(i, tar):
            if i == -1:
                if tar == 0:
                    return 1
                else:
                    return 0
            if (i, tar) in dp:
                return dp[(i, tar)]
            nt = rec(i - 1, tar - nums[i])
            tk = rec(i - 1, tar + nums[i])
            dp[(i, tar)] = nt + tk
            return dp[(i, tar)]

        return rec(len(nums) - 1, t)
