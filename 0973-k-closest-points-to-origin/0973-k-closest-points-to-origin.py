import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic={}
        ans=[]
        for i in range(len(points)):
            dic[i]=math.sqrt((points[i][0]**2)+(points[i][1]**2))
        sorted_dict = sorted(dic.items(), key=lambda x: x[1])
        first_x_keys = [item[0] for item in sorted_dict[:k]]
        for i in first_x_keys:
            ans.append(points[i])
        return ans
        
            