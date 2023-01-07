class Solution:
    def minTimeToType(self, word: str) -> int:
        curr='a'
        ans=0
        for i in range(len(word)):
            if abs(ord(word[i])-ord(curr))>=13:
                ans+=26-abs(ord(word[i])-ord(curr))
                curr=word[i]
            else:
                ans+=abs(ord(word[i])-ord(curr))
                curr=word[i]
        return ans+len(word)