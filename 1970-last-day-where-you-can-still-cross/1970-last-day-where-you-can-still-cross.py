class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        def solve(k):
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            mat=[[0]*n for _ in range(m)]
            for i in range(k):
                mat[cells[i][0]-1][cells[i][1]-1]=1
            q=deque()
            seen=set()
            for j in range(n):
                if mat[0][j]==0:
                    q.append((0,j))
                    seen.add((0,j))
            while q:
                x,y=q.popleft()
                if x==m-1: return True
                for d in directions:
                    nx,ny=x+d[0],y+d[1]
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen and mat[nx][ny]==0:
                        q.append((nx,ny))
                        seen.add((nx,ny))
            return False           
        l=0
        h=m*n
        while l<h:
            mid=l+(h-l+1)//2
            if solve(mid):
                l=mid
            else:
                h=mid-1
        return l 
