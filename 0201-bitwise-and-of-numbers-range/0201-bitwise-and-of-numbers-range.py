class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        ans=0
        for i in range(30,-1,-1):
            if ((l&(1<<i))!=(r&(1<<i))):
                break
            else:
                ans|=(l&(1<<i))
        return ans