class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res=[]
        while i<len(a) and j<len(b):
            a_s,a_e=a[i]
            b_s,b_e=b[j]
            if a_s<=b_e and b_s<=a_e:
                res.append([max(a_s,b_s),min(a_e,b_e)])
            if a_e<=b_e:
                i+=1
            else:
                j+=1
        return res