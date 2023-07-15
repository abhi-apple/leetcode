from collections import deque

class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        stack = deque()
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            if board[i][0] == 1:
                stack.append((i, 0))
                board[i][0] = 0  # Mark as visited
            if board[i][m-1] == 1:
                stack.append((i, m-1))
                board[i][m-1] = 0  # Mark as visited
        for j in range(m):
            if board[0][j] == 1:
                stack.append((0, j))
                board[0][j] = 0  # Mark as visited
            if board[n-1][j] == 1:
                stack.append((n-1, j))
                board[n-1][j] = 0  # Mark as visited
                
        cnt = 0
        dire = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while stack:
            i, j = stack.popleft()
            for d in dire:
                ix, jx = i + d[0], j + d[1]
                if 0 <= ix < n and 0 <= jx < m and board[ix][jx] == 1:
                    stack.append((ix, jx))
                    board[ix][jx] = 0  # Mark as visited
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    cnt += 1
        return cnt
