class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        
        
        dic = {'T':0,'F':0}
        i = 0
        j = 0
        maxi = 0
        while j < len(s):
            if  s[j] in dic:
                dic[s[j]] += 1
            else:
                dic[s[j]] = 1
            
            if (j - i + 1) - max(dic.values()) > k:
                dic[s[i]] -= 1
                i += 1

            j += 1
            maxi = max(maxi, j - i)
            
        return maxi