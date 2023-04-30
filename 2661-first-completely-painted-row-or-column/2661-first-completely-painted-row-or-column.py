class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        row=[0 for i in range(n)]
        col=[0 for j in range(m)]
        dic={}
        for i in range(n):
            for j in range(m):
                dic[mat[i][j]]=[i,j]
        for i in range(len(arr)):
            ind=arr[i]
            st,ed=dic[ind][0],dic[ind][1]
            row[st]+=1
            col[ed]+=1
            if row[st] ==m or col[ed]==n:
                return i
        return -1
                
        