#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        ans=0
        for i in Arr:
            ans^=i
        cnt=0
        while ans>0:
            if 1 & (ans>>cnt)==1:
                break
            cnt+=1
        new=1<<cnt
        zos=[]
        ons=[]
        for i in Arr:
            if new & i==0:
                zos.append(i)
            else:
                ons.append(i)
        ans=[]
        fin=0
        for i in zos:
            fin^=i
        ans.append(fin)
        fin=0
        for i in ons:
            fin^=i
        ans.append(fin)
        ans.sort()
        return ans[::-1]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends