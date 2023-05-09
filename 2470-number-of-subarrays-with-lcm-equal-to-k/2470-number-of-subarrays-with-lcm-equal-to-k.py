import math
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        cnt=0
        def lcm(n1,n2):
            gcd = math.gcd(n1, n2)
            lcm = (n1 * n2) // gcd
            return lcm
        for i in range(len(nums)):
            lcmi=nums[i]
            for j in range(i,len(nums)):
                lcmi=lcm(lcmi,nums[j])
                
                if lcmi==k:
                    cnt+=1
        return cnt
                
            