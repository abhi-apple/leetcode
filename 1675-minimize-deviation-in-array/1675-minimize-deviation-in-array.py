import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sz, maximum, minimum = len(nums), -inf, inf
        for i in range(sz):
            if nums[i] % 2: nums[i] *= 2
        maximum, minimum = max(nums), min(nums)
        minDeviation, maxHeap = maximum - minimum, []
        for i in range(sz):
            heappush(maxHeap, -nums[i])
        while not maxHeap[0] % 2:
            num = -heappop(maxHeap)
            minDeviation = min(minDeviation, num - minimum)
            num //= 2
            minimum = min(minimum, num)
            heappush(maxHeap, -num)
        return min(minDeviation, -maxHeap[0] - minimum)