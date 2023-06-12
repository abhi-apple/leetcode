class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        for i in mat:
            if i[-1]>=tar:
                arr=i[:]
                l=0
                r=len(arr)-1
                while l<=r:
                    mid=(l+r)//2
                    if arr[mid]==tar:
                        return True
                    if arr[mid]>tar:
                        r=mid-1
                    else:
                        l=mid+1
                return False