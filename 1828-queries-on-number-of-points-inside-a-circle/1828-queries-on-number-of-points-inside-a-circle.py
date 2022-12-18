import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res=[]
        for i in queries:
            sums=0
            for j in points:
                if (math.dist(j, i[:2]))<=i[2]:
                    sums+=1
            res.append(sums)
        return res