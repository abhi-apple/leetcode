from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxi = 0
        
        def rec(i, st):
            nonlocal maxi
            if i == len(arr):
                maxi = max(maxi, len(st))
                return 
            
            rec(i + 1, st)
            if len(set(st + arr[i])) == len(st + arr[i]):
                rec(i + 1, st + arr[i])

        rec(0, '')
        return maxi
