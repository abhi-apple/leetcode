class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=''
        for i in num:
            ans=ans+str(i)
        ans=int(ans)
        ans+=k
        ans=str(ans)
        res=[]
        for i in range(len(ans)):
            res.append(int(ans[i]))
            
        return res