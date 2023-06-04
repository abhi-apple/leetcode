class Solution:
    def insert(self, inte: List[List[int]], ne: List[int]) -> List[List[int]]:
        ans=[]
        ad=True
        if not inte:
            return [ne]
        for i in inte:
            if i[0]>ne[0] and ad:
                ad=False
                ans.append(ne)
            ans.append(i)
        if ad:
            ans.append(ne)
        inte=[]
        pre=ans[0]
        for i in ans[1:]:
            if pre[1]>=i[0]:
                pre[1]=max(pre[1],i[1])
            else:
                inte.append(pre)
                pre=i
        inte.append(pre)
        return inte