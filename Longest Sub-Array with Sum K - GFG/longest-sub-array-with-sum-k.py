#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, nums, n, K) : 
        #Complete the function
        prefix_sum = 0
        max_length = 0
        sum_map = {0: -1}  # Stores the prefix sum and its corresponding index
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum - K in sum_map:
                max_length = max(max_length, i - sum_map[prefix_sum - K])
            
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i
        
        return max_length



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends