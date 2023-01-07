from functools import reduce
from heapq import heapify, heappop
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        # Perform the maximum number of operations that we can.
        for i in range(k):
            smallest = heappop(nums)
            heappush(nums, smallest + 1)

        # Calculate the product of the elements in the list.
        res=1
        for x in nums:
            res=(res*x)%(10**9+7)
        return res
