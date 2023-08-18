class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        cnt=[]
        n=len(box)
        m=len(box[0])
        new=[['.' for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if box[i][j]=='*':
                    new[i][j]='*'
        def rotate_matrix_clockwise(matrix):
            rows = len(matrix)
            cols = len(matrix[0])
            new_matrix = [[0] * rows for _ in range(cols)]

            for i in range(rows):
                for j in range(cols):
                    new_matrix[j][rows - 1 - i] = matrix[i][j]

            return new_matrix

        for i in range(n-1,-1,-1):
            cnt=0
            j=m-1
            k=m-1
            while j>=-1:
                
                if j==-1 or  box[i][j]=='*' :
                    b=k
                    while cnt>0:
                        new[i][b]='#'
                        cnt-=1
                        b-=1
                    if j==-1:
                        break
                    j-=1
                    k=j
                elif box[i][j]=='#':
                    cnt+=1
                    j-=1
                else:
                    j-=1
                    
        return rotate_matrix_clockwise(new)
                
                    
                        
                        
                    