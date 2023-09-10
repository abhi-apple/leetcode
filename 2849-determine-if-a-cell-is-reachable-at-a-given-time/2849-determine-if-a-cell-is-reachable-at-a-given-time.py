class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if(fx==sx and fy==sy):
            if(t > 1 or t==0):
                return True
            return False
        
        xDiff = abs(fx-sx)
        yDiff = abs(fy-sy)
       
        return max(xDiff,yDiff) <= t