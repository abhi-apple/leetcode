class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans=[]
        for i in range(left,right+1):
            ans.append(bin(i).count('1'))
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        return sum(1 for n in ans if is_prime(n))