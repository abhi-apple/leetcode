# from typing import List
# from heapq import heappush, heappop
# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         st = sorted([(etime, ptime, i) for i, (etime,ptime) in enumerate(tasks)])
#         t=i=0
#         heap,res=[],[]
#         while len(res)<len(st):
#             while i <len(st) and st[i][0]<=t:
#                 heappush(heap,(st[i][1],st[i][2]))
#                 i+=1
#             if heap:
#                 ptime,i=heappop(heap)
#                 res.append(i)
#                 t+=ptime
#             else:
#                 t=st[i][0]
#         return res
from typing import List
from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        st = sorted([(etime, ptime, i) for i, (etime,ptime) in enumerate(tasks)])
        t=i=0
        heap,res=[],[]
        while len(res)<len(st):
            while i <len(st) and st[i][0]<=t:
                heappush(heap,(st[i][1],st[i][2]))
                i+=1
            if heap:
                ptime,ind=heappop(heap)
                res.append(ind)
                t+=ptime
            else:
                t=st[i][0]
        return res

                