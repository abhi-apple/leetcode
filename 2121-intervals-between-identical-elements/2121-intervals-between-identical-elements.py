class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        ans=[0 for i in range(len(arr))]
        dic={}
        for i,num in enumerate(arr):
            if num not in dic:
                dic[num]=[]
            dic[num].append(i)
        for num,val in dic.items():
            suff=sum(val)
            pref=0
            s=len(val)
            p=0
            for i in val:
                pref+=i
                p+=1
                suff-=i
                s-=1
                ans[i]=p*i-pref +suff-s*i
        return ans
                