#User function Template for python3

from typing import List
import heapq
class Solution:
    
    def minimumMultiplications(self, arr : List[int], st : int, ed : int) -> int:
        # code here
        dis=[float('inf')]*10**5
        dis[st]=0
        que=[]
        heapq.heappush(que,(0,st))
        while que:
            step,node=heapq.heappop(que)
            # print(node)
            if dis[ed]!=float('inf'):
                return dis[ed]
            
            for i in arr:
                if dis[(node*i)%100000]>step+1:
                    dis[(node*i)%100000]=step+1
                    heapq.heappush(que,(step+1,(node*i)%100000))
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends