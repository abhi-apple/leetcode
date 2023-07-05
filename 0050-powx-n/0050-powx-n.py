class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        sign = False
        if n < 0:
            sign = True
            n = -n
        
        def rec(var, po):
            if po == 0:
                return 1
            
            if po & 1 == 0:
                return rec(var * var, po // 2)
            else:
                return var * rec(var, po - 1)
        
        if sign:
            return 1 / rec(x, n)
        
        return rec(x, n)

            