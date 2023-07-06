class Solution:
    def divide(self, div: int, d: int) -> int:
        if div == -2147483648 and d == -1:
            return 2147483647
        if d == 1:
            return div
        sign = -1 if (div >= 0 and d < 0) or (div < 0 and d >= 0) else 1
        div = abs(div)
        d = abs(d)
        res = 0
        
        while div - d >= 0:
            tmp=d
            m=1
            while (tmp<<1)<=div:
            
                tmp=tmp<<1
                m=m<<1
                
            res+=m
            div-=tmp
        return sign*res
        
        
        # tmp = dvs
        # m = 1
        # while (tmp << 1) <= dvd:
        #     tmp <<= 1
        #     m <<= 1  # I am doubling m
        # dvd -= tmp
        # res += m