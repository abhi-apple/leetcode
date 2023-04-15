class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            st=str(num)
            sums=0
            for i in st:
                sums+=int(i)
            num=sums
        return num
            