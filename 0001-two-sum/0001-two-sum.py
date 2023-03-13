class Solution:
    def twoSum(self, main: List[int], tar: int) -> List[int]:
        res=main.copy()
        res.sort()
        i=0
        j=len(res)-1
        ans=[]
        while i<j:
            if res[i]+res[j]==tar:
                n1=res[i]
                n2=res[j]
                break
            elif res[i]+res[j]>tar:
                j-=1
            else:
                i+=1
        for k in range(len(res)):
            if main[k]==n1 or main[k]==n2:
                ans.append(k)
        return ans
            
        
        