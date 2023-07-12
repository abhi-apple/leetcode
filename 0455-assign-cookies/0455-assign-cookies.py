class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=0
        cnt=0
        for i in s:
            
            if j<len(g) and i>=g[j]:
                j+=1
                cnt+=1
        return cnt
#         for i in s:
#             print(j)
#             if j<len(s) and s[j]>=i:
#                 j+=1
#                 cnt+=1
#         return cnt
                
            