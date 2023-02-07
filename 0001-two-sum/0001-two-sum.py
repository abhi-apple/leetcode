class Solution:
    def twoSum(self, main: List[int], tar: int) -> List[int]:
        for i, j in enumerate(main):
            r = tar - j
            if r in main and main.index(r)!=i:
                return [i,main.index(r)]
        
            
        
        