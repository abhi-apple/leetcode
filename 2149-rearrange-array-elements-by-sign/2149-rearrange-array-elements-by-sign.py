from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        fin=[]
        for i in range(len(pos)):
            fin.append(pos[i])
            fin.append(neg[i])
        return fin
