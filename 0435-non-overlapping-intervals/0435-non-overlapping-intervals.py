class Solution:
    def eraseOverlapIntervals(self, inte: List[List[int]]) -> int:
        inte.sort()
        st=inte[0][1]
        cnt=0
        for i in inte[1:]:
            if i[0]<st:
                
                cnt+=1
                st=min(st,i[1])
            else:
                st=i[1]
        return cnt