class Solution:
    def numOfBurgers(self, ts: int, cs: int) -> List[int]:
        if ts%2==0 and cs*2<=ts and ts<=cs*4:
            jumbo = (ts - cs*2)//2
            small = cs - jumbo
            if jumbo >= 0 and small >= 0 and jumbo == int(jumbo) and small == int(small):
                return [int(jumbo), int(small)]
        return []