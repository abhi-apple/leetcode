class Solution:
    def change(self, a: int, co: List[int]) -> int:
        dic={}
        def rec(i,am):
            if am==0:
                return 1
            if am<0 or i<0:
                return 0
            if (i,am) in dic:
                return dic[(i,am)]
            nt=rec(i-1,am)
            dic[(i,am)]=nt+rec(i,am-co[i])
            return dic[(i,am)]
        return rec(len(co)-1,a)