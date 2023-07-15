from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: (x[0], x[1]))
        
        @lru_cache(None)
        def dp(idx, max_end, k):
            if idx < 0 or k == 0:
                return 0
            if events[idx][1] <= max_end:
                return max(
                    dp(idx-1, max_end, k),
                    dp(idx-1, events[idx][0] - 1, k-1) + events[idx][2]
                )
            else:
                return dp(idx-1, max_end, k)
       
        return dp(len(events) - 1, float('inf'), k)
                