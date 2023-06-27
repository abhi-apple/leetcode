class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis=set()
   
        que=deque()
        def bfs(i,j):
            nonlocal que
            cnt=0
            vis.add((i,j))
            
            while que:
                size = len(que)  # Number of oranges at the current level (minute)
                for _ in range(size):
                    i, j = que.popleft()
                    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for d in directions:
                        ix, jx = i + d[0], j + d[1]
                        if (ix, jx) not in vis and 0 <= ix < len(grid) and 0 <= jx < len(grid[0]) and grid[ix][jx] == 1:
                            vis.add((ix, jx))
                            que.append((ix, jx))
                            grid[ix][jx] = 2
                if que:  # Increment minutes if there are more oranges at the next level
                    cnt += 1
            return cnt
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                 if grid[i][j]==2:
                        que.append([i,j])
        if not que:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        return -1
            return 0
        i,j=que[0]
        ans=bfs(i,j)
        print(ans)
    
                    
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return ans