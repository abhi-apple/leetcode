class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sums=0
        prev=0
        for i in bank:
            n=i.count('1')
            if n>0:
                sums+=prev*n
                prev=n
        return sums
                