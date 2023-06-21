from typing import List

class Solution:
    def f(self, A: List[int], cost: List[int], x: int) -> int:
        res = 0
        for i in range(len(A)):
            res += abs(A[i] - x) * cost[i]
        return res

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        total = 0
        _sum = 0
        median = 0
        v = []
        
        for i in range(len(nums)):
            v.append((nums[i], cost[i]))
        
        v.sort()
        
        for i in range(len(cost)):
            _sum += v[i][1]
        
        i = 0
        while total < (_sum + 1) // 2 and i < len(nums):
            total += v[i][1]
            median = v[i][0]
            i += 1
        
        return self.f(nums, cost, median)
