class Solution:
    def merge(self, ans: List[List[int]]) -> List[List[int]]:
        ans.sort()
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