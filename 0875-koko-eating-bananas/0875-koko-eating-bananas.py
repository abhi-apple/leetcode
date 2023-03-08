class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1  # start from 1 instead of using ceil(sum(piles) / h)
        right = max(piles)
        while left < right:
            mid = (left + right) // 2  # use integer division
            total_time = 0
            for pile in piles:
                total_time += (pile + mid - 1) // mid  # use ceiling division
                if total_time > h:
                    break
            if total_time <= h:
                right = mid
            else:
                left = mid + 1
        return right
