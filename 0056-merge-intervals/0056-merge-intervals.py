class Solution:
    def merge(self, inter: List[List[int]]) -> List[List[int]]:
        res=[]
        if len(inter)==0:
            return res
        inter.sort()
        temp=inter[0]
        for i in inter:
            if i[0]<=temp[1]:
                temp[1]=max(i[1],temp[1])
            else:
                res.append(temp)
                temp=i
        res.append(temp)
        return res
            