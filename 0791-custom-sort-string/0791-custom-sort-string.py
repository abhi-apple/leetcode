class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=""
        for i in order:
            for k in range(s.count(i)):
                ans+=i
        for a in s:
            if a not in order:
                ans+=a
        return ans