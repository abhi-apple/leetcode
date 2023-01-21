class Solution:
    def twoSum(self, main: List[int], tar: int) -> List[int]:
        d = {}
        for i, j in enumerate(main):
            r = tar - j
            if r in d: return [d[r], i]
            d[j] = i
        
            
        
        