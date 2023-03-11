
# class Solution:
#     def rotate(self, mat: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
        
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
#         for i in range(len(mat)):
#             mat[i].reverse()
        
class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Reverse the rows of the matrix
        mat.reverse()
        print(mat)
        # Swap the elements of the matrix
        for i in range(len(mat)):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            