#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        sums=sum(arr)
        main=n*(n+1)//2
        dub=0
        ans=[False for i in range(n+1)]
        for i in range(n):
            if ans[arr[i]]:
                dub=arr[i]
            else:
                ans[arr[i]]=True
        for i in range(len(ans)):
            if not ans[i]:
                mis=i
        return [dub,mis]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends