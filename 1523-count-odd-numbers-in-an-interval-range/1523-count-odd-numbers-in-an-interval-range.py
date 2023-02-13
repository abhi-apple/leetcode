class Solution:
    def countOdds(self, l: int, h: int) -> int:
        if l & 1==1 and h&1==1:
            return ((h-l-1)//2)+2
        elif (l & 1 ==1 and h &1==0) or (h & 1 ==1 and l &1==0):
            return ((h-l-1)//2)+1
        else:
            return ((h-l-1)//2)+1
        