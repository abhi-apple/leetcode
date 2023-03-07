# class Solution:
#     def minimumTime(self, time: List[int], totalTrips: int) -> int:
#         tot=0
#         time.sort()
#         tim=1
#         while tot<totalTrips:
#             for i in time:
#                 if tim%i==0:
#                     tot+=1
#             tim+=1
#         return tim
from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = max(time) * totalTrips
        
        while left < right:
            mid = (left + right) // 2
            
            trips = sum(mid // t for t in time)
            
            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
        
        return left
