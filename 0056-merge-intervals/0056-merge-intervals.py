class Solution:
    def merge(self, intr: List[List[int]]) -> List[List[int]]:
        res=[]
        if len(intr)==1:
            return intr
        intr.sort()
        temp=intr[0]
        for i in intr[1:]:
            if temp[1]>=i[0]:
                temp[1]=max(temp[1],i[1])
            else:
                res.append(temp)
                temp=i
        res.append(temp)
        return res