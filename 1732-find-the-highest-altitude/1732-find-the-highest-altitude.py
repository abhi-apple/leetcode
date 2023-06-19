class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        st=0
        maxi=0
        prev=0
        for i in gain:
            val=prev+i
            maxi=max(maxi,val)
            prev=val
        return maxi
            