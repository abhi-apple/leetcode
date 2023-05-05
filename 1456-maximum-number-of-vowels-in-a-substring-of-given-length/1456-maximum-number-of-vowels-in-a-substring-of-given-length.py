class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k
        s = list(s)
        vowels = set(["a", "e", "i", "o", "u"])
        maxi = 0
        cnt = 0
        for ind in range(len(s)):
            if s[ind] in vowels:
                cnt += 1
            if ind >= k and s[ind - k] in vowels:
                cnt -= 1
            maxi = max(maxi, cnt)
        # if ind >= j-1:
        #     return maxi
        return maxi

            