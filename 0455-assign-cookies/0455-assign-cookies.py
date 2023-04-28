class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        j=0
        cnt=0
        g.sort()
        s.sort()
        while i<len(g) and j <len(s):
            if s[j]>=g[i]:
                i+=1
                j+=1
                cnt+=1
            else:
                j+=1
        return cnt