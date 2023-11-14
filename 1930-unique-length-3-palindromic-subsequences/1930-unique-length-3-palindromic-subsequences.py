class Solution:
    def countPalindromicSubsequence(self, s):
        res = 0


        for k in string.ascii_lowercase:
            first, last = s.find(k), s.rfind(k)
            if first > -1:
                res += len(set(s[first + 1: last]))
        return res