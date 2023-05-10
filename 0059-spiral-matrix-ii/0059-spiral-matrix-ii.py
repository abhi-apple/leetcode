from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        top, bot, left, right = 0, n - 1, 0, n - 1
        ct = 0
        while ct<n*n:
            for i in range(left,right+1):
                ct+=1
                matrix[top][i]=ct
            top+=1
            if top>bot:
                break
            for i in range(top,bot+1):
                ct+=1
                matrix[i][right]=ct
            right-=1
            if left>right:
                break
            for i in range(right,left-1,-1):
                ct+=1
                
                matrix[bot][i]=ct
            bot-=1
            if top>bot:
                break
            for i in range(bot,top-1,-1):
                ct+=1
                matrix[i][left]=ct
            left+=1
            if left>right:
                break
                
        return matrix
