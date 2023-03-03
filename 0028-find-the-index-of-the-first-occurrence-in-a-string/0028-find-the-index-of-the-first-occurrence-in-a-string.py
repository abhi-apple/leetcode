class Solution:
    def strStr(self, h: str, n: str) -> int:
        i=0
        j=len(n)
        if j==len(h):
            if h==n:
                return 0
            else:
                return -1
        while j<=len(h):
    
            if n==h[i:j]:
                return i
            i+=1
            j+=1
        return -1