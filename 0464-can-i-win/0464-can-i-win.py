class Solution:
    def canIWin(self, maxch: int, tot: int) -> bool:
        cad = list(range(1, maxch + 1))
        if sum(cad) < tot:
            return False
        @cache
        def rec(arr,sums):
            if arr[-1]>=sums:
                return True
            for i in range(len(arr)):
                if not rec(arr[:i]+arr[i+1:],sums-arr[i]):
                    return True
            return False
        return rec(tuple(cad),tot)
            