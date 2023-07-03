#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i=0
        j=0
        ans=[]
        while i<n and j<m:
            if a[i]==b[j] :
                if not ans or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
                j+=1
                    
            elif a[i]>b[j]:
                if not ans or ans[-1]!=b[j]:
                    ans.append(b[j])
                j+=1
            else:
                if not ans or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
        while i<n:
            if not ans or ans[-1]!=a[i]:
                ans.append(a[i])
            i+=1
        while j<m:
            if not ans or ans[-1]!=b[j]:
                ans.append(b[j])
            j+=1
        return ans
        
                
                    
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends