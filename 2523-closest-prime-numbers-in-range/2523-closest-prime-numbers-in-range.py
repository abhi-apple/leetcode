class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        pair=[-1,-1]
        q=[]
        diff=float('inf')
        def is_prime(n):
            if n < 2:  # Numbers less than 2 are not prime
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        for i in range(left,right+1):
            if is_prime(i):
                q.append(i)
            while len(q)>=2:
                if abs(q[0]-q[1])<diff:
                    pair=[q[0],q[1]]
                    diff=abs(q[0]-q[1])
                    if diff<=2:
                        return pair
                q.pop(0)
        return pair
                    
            