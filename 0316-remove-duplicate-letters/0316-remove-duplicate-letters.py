class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i
        ans=[]
        for i in range(len(s)):
            if s[i] not in ans:
                while ans and s[i]<ans[-1] and i<dic[ans[-1]]:
                    ans.pop()
                ans.append(s[i])
        return ''.join(ans)
        