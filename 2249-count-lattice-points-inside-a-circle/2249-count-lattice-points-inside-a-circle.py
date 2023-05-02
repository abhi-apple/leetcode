from typing import List

class Solution:
    def countLatticePoints(self, cir: List[List[int]]) -> int:
        res=set()
        
        def find(x,y,z):
            for i in range(x-z,x+z+1):
                for j in range(y-z,y+z+1):
                    if (x-i)**2 + (y-j)**2 <=z**2:
                        res.add((i,j))
            
            
        
        for i in cir:
            find(i[0],i[1],i[2])
            
        print(res)
        return len(res)
            
