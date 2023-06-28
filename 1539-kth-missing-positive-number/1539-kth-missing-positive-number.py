class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        j=len(arr)-1
        while i<=j:
            mid=(i+j)//2
            mis=arr[mid]-(mid+1)
            if mis<k:
                i=mid+1
            else:
                j=mid-1
        return k+i
            