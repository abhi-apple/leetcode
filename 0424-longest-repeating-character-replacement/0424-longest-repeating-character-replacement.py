# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         dic={}
#         i=0
#         j=0
#         dic[s[i]]=1
#         while j<len(s):
#             if j!=0 and s[j] in dic:
#                 dic[s[j]]+=1
#             else:
#                 dic[s[j]]=1
#             if (j-i+1)-max(dic.values())>=k:
#                 j+=1
#             else:
#                 i-=1
#                 dic[s[i+1]]-=1
#             maxi=max(maxi,(j-i+1))
#         return maxi

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        i = 0
        j = 0
        maxi = 0
        dic[s[i]] = 1
        while j < len(s):
            if j != 0 and s[j] in dic:
                dic[s[j]] += 1
            else:
                dic[s[j]] = 1
            
            if (j - i + 1) - max(dic.values()) > k:
                dic[s[i]] -= 1
                i += 1

            j += 1
            maxi = max(maxi, j - i)
            
        return maxi
