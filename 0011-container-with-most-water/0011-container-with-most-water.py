class Solution:
    def maxArea(self, he: List[int]) -> int:
        maxi=0
        i=0
        j=len(he)-1
        while i<j:
            hei=min(he[i],he[j])
            
            maxi=max(maxi,hei*(j-i))
            
            while he[i]<=hei and i<j:
                i+=1
            while he[j]<=hei and i<j:
                j-=1
        return maxi
                