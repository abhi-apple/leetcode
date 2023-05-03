class Solution:
    def sumBase(self, n: int, k: int) -> int:
        x=[]
        while n!=0:
            x.append(n%k)
            n=n//k
            
        return sum(x)