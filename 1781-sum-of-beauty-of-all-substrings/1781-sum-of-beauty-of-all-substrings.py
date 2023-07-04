class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            fre=[0]*26
            for j in range(i,len(s)):
                fre[ord(s[j])-ord('a')]+=1
                mini=float('inf')
                for i in fre:
                    if i!=0:
                        mini=min(mini,i)
                ans+=max(fre)-mini
        return ans