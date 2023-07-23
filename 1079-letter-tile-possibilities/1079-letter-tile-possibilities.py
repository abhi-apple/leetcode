class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        fin=set()
        n=len(tiles)
        dic={i:0 for i in range(n)}
        stri=''
        def rec():
            nonlocal stri,dic,fin
            for i in range(n):
                if dic[i]==0:
                    dic[i]=1
                    stri=stri+tiles[i]
                    fin.add(stri)
                    
                    rec()
                    stri=stri[:-1]
                    dic[i]=0
        rec()
        return len(fin)
                    
                    
                    