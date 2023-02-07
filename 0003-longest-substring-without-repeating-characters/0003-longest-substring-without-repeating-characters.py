class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p=list(s)
        res=[]
        if not p:
            return 0
        res.append(p[0])
        maxi=1
        for i in range(1,len(p)):
            while p[i] in res and res:
                res.pop(0)
            res.append(p[i])
            maxi=max(maxi,len(res))
        return maxi
                