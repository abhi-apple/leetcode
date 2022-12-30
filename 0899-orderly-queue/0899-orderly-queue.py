class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return "".join(sorted(s))
        result = s
        for i in range(len(s)):
            s = s[1:] + s[0]
            result=min(result,s)
        return result

        