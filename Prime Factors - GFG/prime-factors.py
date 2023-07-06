#User function Template for python3

class Solution:
    def AllPrimeFactors(self, n):
        # Code here
        if n in [0, 2, 3]:
            return [n]

        ans = []
        for k in range(2, int(n**0.5) + 1):
            if n % k == 0:
                while n % k == 0:
                    n //= k
                ans.append(k)

        if n > 1:
            ans.append(n)

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends