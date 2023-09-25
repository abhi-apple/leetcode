class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        for i in t:
            if i not in s:
                
                return i
            else:
                s.remove(i)
        return t[-1]
            
        