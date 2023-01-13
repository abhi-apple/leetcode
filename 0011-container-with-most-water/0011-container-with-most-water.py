class Solution:
    def maxArea(self, he: List[int]) -> int:
        i=0
        j=len(he)-1
        wat=0
        while i<j:
            h=min(he[i],he[j])
            wat=max(wat,h*(j-i))
            while he[i]<=h and i<j:
                i+=1
            while he[j]<=h and i<j:
                j-=1
        return wat
            
            
            