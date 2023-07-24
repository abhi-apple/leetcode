class Solution:
    def reorganizeString(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        if sorted(dic.values())[-1]>(len(s)+1)//2:
            return ''
        new=[]
        for i in dic:
            val=dic[i]
            new.append([i]*val)
        final=''
        new.sort(key=len,reverse=True)
        while new[0]!=[]:
            i=0
           
            while final and i<len(new) and new[i] and new[i][0]==final[-1]:
                
                i+=1
            final=final+new[i].pop()
            new.sort(key=len,reverse=True)
        if not final:
            return ''
        return final