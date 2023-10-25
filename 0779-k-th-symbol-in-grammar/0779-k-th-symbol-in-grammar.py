class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1: 
            return 0
        mid=math.pow(2,n-1)//2
        if k<=mid:
            return self.kthGrammar(n-1,k) 
        else:
            return 1-self.kthGrammar(n-1,k-mid) 