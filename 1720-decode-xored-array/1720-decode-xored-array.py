class Solution:
    def decode(self, enc: List[int], fir: int) -> List[int]:
        ans=[]
        ans.append(fir)
        for i in enc:
            ans.append(fir^i)
            fir=fir^i
        return ans