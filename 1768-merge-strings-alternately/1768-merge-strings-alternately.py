class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        ans = ''
        for i in range(max(len(w1), len(w2))):
            if i < len(w1):
                ans += w1[i]
            if i < len(w2):
                ans += w2[i]
        return ans


            