class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        stcol=0
        edcol=len(mat[0])-1
        while stcol<=edcol:
       
            maxir=0
            mid=(edcol+stcol)//2
            for row in range(len(mat)):
                maxir=row if mat[row][mid]>=mat[maxir][mid] else maxir
            leftbig=mid-1>=stcol and mat[maxir][mid]<mat[maxir][mid-1]
            rgtbig= mid+1<=edcol and mat[maxir][mid]<mat[maxir][mid+1]
            if not leftbig and not rgtbig:
                return [maxir,mid]
            elif leftbig:
                edcol=mid-1
                
            else:
                stcol=mid+1
                
     
        return []
    
    
# class Solution(object):
#     def findPeakGrid(self, mat):
#         startCol = 0
#         endCol = len(mat[0])-1
       
#         while startCol <= endCol:
#             maxRow = 0
#             midCol = (endCol+startCol)//2
            
#             for row in range(len(mat)):
#                 maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
            
#             leftIsBig    =   midCol-1 >= startCol  and  mat[maxRow][midCol-1] > mat[maxRow][midCol]
#             rightIsBig   =   midCol+1 <= endCol    and  mat[maxRow][midCol+1] > mat[maxRow][midCol]
            
#             if (not leftIsBig) and (not rightIsBig):   # we have found the peak element
#                 return [maxRow, midCol]
#             elif rightIsBig:             # if rightIsBig, then there is an element in 'right' that is bigger than all the elements in the 'midCol', 
#                 startCol = midCol+1     # so 'midCol' cannot have 'peakPlane'
#             else:                           # leftIsBig
#                 endCol = midCol-1
                
#         return []