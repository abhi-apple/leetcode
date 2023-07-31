class Solution:
    def countTexts(self, pres: str) -> int:
        dp={}
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        n=len(pres)
        @cache
        def rec(i):
            if i==n:
                return 1
            tot=0
            for j in range(len(dic[pres[i]])):
                k=i+j+1
                if k>len(pres) or pres[i]!=pres[k-1]:
                    break
                tot=(tot+rec(k))%(10**9 +7)
            return tot%(10**9 +7)
        return rec(0)
                    
            