import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        now = copy.deepcopy(board)  # Use deepcopy to create a deep copy
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                lv = 0
                nnlv = 0

                if now[i][j] == 0:
                    liv = False
                else:
                    liv = True

                dire = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                for d in dire:
                    ix, jx = i + d[0], j + d[1]
                    if 0 <= ix < n and 0 <= jx < m:
                        if now[ix][jx] == 0:
                            nnlv += 1
                        else:
                            lv += 1

                if liv and (lv < 2 or lv > 3):
                    board[i][j] = 0
                elif not liv and (lv == 3):
                    board[i][j] = 1

                    