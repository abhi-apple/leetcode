class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        m = (10**9) + 7

        def fact(n):
            r = 1
            for i in range(1, n+1):
                r = (r * i) % m
            return r

        def combs(n, r):
            nr = fact(n)
            dr = (fact(r) * fact(n - r)) % m
            return (nr * pow(dr, m - 2, m)) % m

        def countBST(nums):
            if len(nums) <= 2:
                return 1

            left_nums = [n for n in nums if n < nums[0]]
            right_nums = [n for n in nums if n > nums[0]]

            left_count = countBST(left_nums)
            right_count = countBST(right_nums)

            return (combs(len(nums) - 1, len(left_nums)) * left_count * right_count) % m

        return (countBST(nums) - 1) % m