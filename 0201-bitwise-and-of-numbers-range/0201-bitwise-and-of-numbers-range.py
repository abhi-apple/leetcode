class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        i=0
        while l<r:
            l>>=1
            r>>=1
            i+=1
        return l<<i