class Solution:
    def suggestedProducts(self, prod: List[str], sea: str) -> List[List[str]]:
        ans=[]
        for i in range(len(prod)):
            if sea[0]==prod[i][0]:
                ans.append(prod[i])
        fin=[]
        ans.sort()
        print(ans)
        if len(ans)>=3:
            fin.append(ans[:3])
        else:
            fin.append(ans)
    
        for i in range(1,len(sea)):
            prod=ans.copy()
            ans=[]
            for j in prod:
                if sea[:i+1]==j[:i+1]:
                    ans.append(j)
            if len(ans)>=3:
                fin.append(ans[:3])
            else:
                fin.append(ans)
        return fin
            
                    
            
            