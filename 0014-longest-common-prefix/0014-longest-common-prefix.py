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
        ans=''
        st=sorted(st)
        n=min(len(st[0]),len(st[-1]))
        for i in range(n):
            if st[0][i]!=st[-1][i]:
                return ans
            ans=ans+st[0][i]
            
        return ans
                