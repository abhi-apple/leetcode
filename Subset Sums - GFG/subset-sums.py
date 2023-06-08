#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		arr.sort()
		ans=[]
		def rec(i,sums):
		    if i==N:
		        ans.append(sums)
		        return 
		    rec(i+1,sums)
		    rec(i+1,sums+arr[i])
		    return 
		rec(0,0)
		return ans
		  
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends