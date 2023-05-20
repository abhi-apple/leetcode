class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums = sorted(list(set(nums)))
        memo = {}

        def earn(start):
            if start >= len(nums):
                return 0

            if start in memo:
                return memo[start]

            earn_without_current = earn(start + 1)

            if start + 1 < len(nums) and nums[start] == nums[start + 1] - 1:
                skip = nums[start] * cnt[nums[start]] + earn(start + 2)
            else:
                skip = nums[start] * cnt[nums[start]] + earn(start + 1)

            result = max(earn_without_current, skip)
            memo[start] = result
            return result

        return earn(0)
