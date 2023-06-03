class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=1
        if s=="":
            return 0
        maxi=1
        while j<len(s):
            while s[j] in s[i:j]:
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
            
        return maxi