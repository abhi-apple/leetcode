class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        st=[]
        for i in range(n):
            j=0
            new=[]
            k=i
            while k<n and j<m:
                new.append(mat[k][j])
                k+=1
                j+=1
            st.append(sorted(new))
        for j in range(1,m):
            i=0
            new=[]
            k=j
            while k<m and i<n:
                new.append(mat[i][k])
                i+=1
                k+=1
            st.append(sorted(new))
        for i in range(n):
            j=0
            k=i
            now=st.pop(0)
            
            while k<n and j<m:
                mat[k][j]=now.pop(0)
                k+=1
                j+=1
        for j in range(1,m):
            i=0
            now=st.pop(0)
            k=j
            while k<m and i<n:
                mat[i][k]=now.pop(0)
                i+=1
                k+=1
                
        return mat
            
                
            