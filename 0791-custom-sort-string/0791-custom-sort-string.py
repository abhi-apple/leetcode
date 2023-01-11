class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pos = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda c: pos.get(c, len(order))))
        # dic={}
        # for i in range(len(order)):
        #     dic[order[i]]=i
        # ans={}
        # i=len(s)
        # for j in range(len(s)):
        #     if s[j] in dic:
        #         ans[s[j]]=dic[s[j]]
        #     else:
        #         ans[s[j]]=i
        #         i+=1
        # sorted_d = sorted(ans, key=ans.get)
        # return ''.join(sorted_d)