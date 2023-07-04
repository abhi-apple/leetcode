class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        fin=sorted(dic.items(), key=lambda x:x[1],reverse=True)
        res=''
        for st,val in fin:
            res=res+st*val
        return res