class Solution:
    def search(self, arr: List[int], tar: int) -> int:
        i=0
        j=len(arr)-1
        while i<=j:
            mid=(i+j)//2
            if arr[mid]==tar:
                return mid
            if arr[i]<=arr[mid]:
                if arr[i]<=tar<=arr[mid]:
                    j=mid-1
                else:
                    i=mid+1
                    
            else:
                if arr[mid]<=tar<=arr[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1
                    
                