class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        j=0
        p=0
        for i in range(1,arr[-1]):
            if arr[j]!=i:
                p+=1
            else:
                j+=1
                
            if p==k:
                return i
        return arr[-1]+(k-p)