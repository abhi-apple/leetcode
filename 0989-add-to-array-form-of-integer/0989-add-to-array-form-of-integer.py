class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=[]
        st=''
        for i in num:
            ans.append(str(i))
        ars=int(st.join(ans))
        ans=[]
        ars=ars+k
        for i in str(ars):
            ans.append(int(i))
        return ans