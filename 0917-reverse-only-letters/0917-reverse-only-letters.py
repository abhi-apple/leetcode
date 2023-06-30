class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        rev=[]
        alp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in s:
            if i in alp:
                rev+=i
        for i in range(len(s)):
            if s[i] in alp:
                s[i]=rev.pop()
        return ''.join(s)
            