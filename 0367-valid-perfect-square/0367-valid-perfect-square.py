class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        nums=0
        cnt=0
        while nums<num:
            cnt+=1
            nums=cnt*cnt
        if nums==num:
            return True
        return False