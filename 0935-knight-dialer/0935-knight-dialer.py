from functools import cache

class Solution:
    def knightDialer(self, n: int) -> int:
        count = 0
        
        @cache
        def rec(i, j, cnt):
            nonlocal count
            
            if cnt == 0:
                return 1
            
            dire = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
            total = 0
            
            for d in dire:
                ix, jx = i + d[0], j + d[1]
                
                if 0 <= ix < 4 and 0 <= jx < 3 and (ix, jx) != (3, 0) and (ix, jx) != (3, 2):
                    total += rec(ix, jx, cnt - 1)
            
            return total
        
        for i in range(3):
            for j in range(3):
                count += rec(i, j, n - 1)
        count+=rec(3,1,n-1)
        
        return count % (10**9 + 7)