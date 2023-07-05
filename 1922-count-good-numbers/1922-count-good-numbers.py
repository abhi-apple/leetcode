import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 +7
        def rec(var, po):
            if po == 0:
                return 1
            
            if po & 1 == 0:
                return rec((var * var)%mod, po // 2)
            else:
                return ((var)%mod) * ((rec(var, po - 1))%mod)
        if n & 1==0:
            return (rec(20,n//2))%mod
        else:
            return (rec(20,n//2)*5)%mod