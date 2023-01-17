class Solution:
    def merge(self, intr: List[List[int]]) -> List[List[int]]:
        res=[]
        if len(intr)==0:
            return res
        intr.sort()
        tem=intr[0]
        for i in intr:
            if tem[1]>=i[0]:
                tem[1]=max(i[1],tem[1])
            else:
                res.append(tem)
                tem=i
        res.append(tem)
        return res