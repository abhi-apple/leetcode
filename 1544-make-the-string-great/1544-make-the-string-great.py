class Solution:
    def makeGood(self, s: str) -> str:
        result=[]
        for i in range(len(s)):
            if result and abs(ord(s[i]) - ord(result[-1])) == 32:
                result.pop()
            else:
                result.append(s[i])
        return ''.join(result)