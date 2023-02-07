# class Solution:
#     def longestCommonPrefix(self, st: List[str]) -> str:
#         mini=1000
#         for i in range(len(st)):
#             mini=min(mini,len(st[i]))
#         ans=st[0]
#         ans=ans[:mini]
#         for i in range(len(st)):
#             for j in range(len(ans)):
#                 print(ans[j])
#                 print(st[i][j])
#                 if ans[j]==st[i][j]:
#                     continue
#                 else:
#                     ans=ans[:j]
#         return ans
class Solution:
    def longestCommonPrefix(self, st: List[str]) -> str:
        if len(st) == 0:
            return ""
        if len(st) == 1:
            return st[0]

        mini = min([len(s) for s in st])
        ans = st[0][:mini]

        for i in range(1, len(st)):
            j = 0
            while j < len(ans) and j < len(st[i]) and ans[j] == st[i][j]:
                j += 1
            ans = ans[:j]
            if len(ans) == 0:
                return ""
        return ans
