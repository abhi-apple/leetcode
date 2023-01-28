from bisect import bisect_left

class Solution:
    def findRightInterval(self, ite: List[List[int]]) -> List[int]:
        n = len(ite)
        starts = [i[0] for i in ite]
        ends = [i[1] for i in ite]
        starts_index = [(val, index) for index, val in enumerate(starts)]
        starts_index.sort()
        res = []

        for end in ends:
            index = bisect_left(starts_index, (end,))
            if index < n:
                res.append(starts_index[index][1])
            else:
                res.append(-1)

        return res

                    
        # for i in range(len(ls)):
            
            