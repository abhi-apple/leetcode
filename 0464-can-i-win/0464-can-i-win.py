class Solution:
    def canIWin(self, maxch: int, tot: int) -> bool:
        cad = list(range(1, maxch + 1))
        if sum(cad) < tot:
            return False
        # @cache
        dp={}
        def rec(arr,sums):
            if arr[-1]>=sums:
                return True
            if (arr,sums) in dp:
                return dp[(arr,sums)]
           
            for i in range(len(arr)):
                if not rec(arr[:i]+arr[i+1:],sums-arr[i]):
                    dp[(arr,sums)]=True
                    return True
            dp[(arr,sums)]=False
            return False
        return rec(tuple(cad),tot)
            