class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sums=0
        prev=0
        for i in bank:
            if i.count('1')>0:
                sums+=prev*i.count('1')
                prev=i.count('1')
        return sums
                