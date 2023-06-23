class Solution:
    def minSubArrayLen(self, tar: int, nums: List[int]) -> int:
        sums=sum(nums)
        if sums< tar:
            return 0
        n = len(nums)
        if sums == tar:
            return n
        
        sums = 0
        j = 0
        while sums <tar:
            sums += nums[j]
            j += 1

            
        
        maxi = float('inf')
        i = 0
        while j < n+1:
            
            if sums >= tar:
        
                maxi = min(maxi, j - i )
                
                sums -= nums[i]
                i += 1
            else:
                if j<n:
                    
                    sums += nums[j]
                j += 1
#                 if j < n - 1:
                 
#                     j += 1
                    
#                     print(j,sums)
#                 else:
                    
#                     print('hi')
#                     break
        return maxi

                
        