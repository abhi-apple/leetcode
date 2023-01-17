class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        ans=[]
        if len(mat)==1:
            if tar in mat[0]:
                return True
        for i in range(len(mat)):
            if mat[i][0]==tar:
                return True
            if mat[i][0]>tar:
                if i-1==-1:
                    return False
                ans=mat[i-1]
                break
        if len(ans)==0:
            if tar in mat[-1]:
                return True
        if tar in ans:
            return True
        return False