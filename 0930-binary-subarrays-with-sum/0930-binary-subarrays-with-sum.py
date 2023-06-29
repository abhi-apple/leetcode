# from collections import defaultdict

# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         prev = []
#         sums = 0
#         res = 0
#         dic = defaultdict(int)
#         for i in nums:
#             sums += i
#             prev.append(sums)
#         for k in prev:
#             cnt = k - goal
#             res += dic[cnt]
#             dic[k] += 1
#         return res

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sums = [0]
        result = 0
        count = defaultdict(int)
        count[0] = 1

        # Calculate prefix sums
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        # Count subarrays with sum equal to the goal
        for i in range(len(nums)):
            complement = prefix_sums[i + 1] - goal
            result += count[complement]
            count[prefix_sums[i + 1]] += 1

        return result
