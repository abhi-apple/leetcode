class Solution:
    def digitCount(self, num: str) -> bool:
        k=0
        for i in num:
            print(num.count(str(k)),int(i))
            if num.count(str(k))!=int(i):
                return False
            k+=1
        return True