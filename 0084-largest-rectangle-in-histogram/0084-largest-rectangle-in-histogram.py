import bisect
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        n=len(h)
        nsl=[0]*n
        nsr=[0]*n
        s=[]
        for i in range(n-1,-1,-1):
            while s and h[i]<=h[s[-1]]:
                s.pop()
            if not s:
                nsr[i]=n
            else:
                nsr[i]=s[-1]
            s.append(i)
        s=[]
        for i in range(n):
            while s and h[i]<=h[s[-1]]:
                s.pop()
            if not s:
                nsl[i]=-1
            else:
                nsl[i]=s[-1]
            s.append(i)
        ans=0
        for i in range(n):
            ans=max(ans,h[i]*(nsr[i]-nsl[i]-1))
        return ans