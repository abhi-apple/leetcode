class Solution:
    def partitionString(self, s: str) -> int:
        l=0
        r=0
        ans=0
        v=""
        while r<len(s):
            if s[r] not in v:
                v+=s[r]
                # print(v,"if")
                r+=1
            else:
                ans+=1
                l=r
                v=""
                # print(v,"else")
        return ans+1
                