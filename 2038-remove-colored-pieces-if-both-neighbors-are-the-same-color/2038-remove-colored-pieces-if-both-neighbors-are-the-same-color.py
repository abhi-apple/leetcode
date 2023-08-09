class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        dic={'A':[],'B':[]}
        i=0
        while i<n:
            if colors[i]=='A':
                cnt=0
                while i<n and colors[i]=='A'  :
                    cnt+=1
                    i+=1
                dic['A'].append(cnt)
            else:
                cnt=0
                while i<n and colors[i]=='B':
                    cnt+=1
                    i+=1
                dic['B'].append(cnt)
        alis=0
        for i in dic['A']:
            if i>=3:
                alis+=1
                i=i-3
                if i>0:
                    alis+=i
                    i=0
        bobs=0
        for i in dic['B']:
            if i>=3:
                bobs+=1
                i=i-3
                if i>0:
                    bobs+=i
                    i=0
        
        
        return alis>bobs
                
                    
            
            