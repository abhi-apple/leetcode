# class Solution:
#     def calculateMinimumHP(self, grid: List[List[int]]) -> int:
#         dp={}
#         n=len(grid)
#         m=len(grid[0])
#         ans=[]
#         def rec(i,j,arr):
            
#             if (i,j) in dp:
#                 return dp[(i,j)]
#             if i==n-1 and j==0:
#                 arr.append(min(arr[-1]+grid[i][j],grid[i][j]))
#                 # print(arr)
#                 ans.append(min(arr))
#                 return grid[i][j]
#             if 0>i or i>n-1 or 0>j or j>m-1:
#                 return -float('inf')
#             dp[(i,j)]=max(rec(i+1,j,arr+[min(arr[-1]+grid[i][j],grid[i][j])]),rec(i,j+1,arr+[min(arr[-1]+grid[i][j],grid[i][j])]))+grid[i][j]
#             return dp[(i,j)]
        
#         rec(0,0,[0])
#         return -max(ans)+1
        
    
from typing import List

class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        dp = {}
        n = len(grid)
        m = len(grid[0])

        def rec(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == n - 1 and j == m - 1:
                return max(1 - grid[i][j], 1)
            
            if i >= n or j >= m:
                return float('inf')
            
            right = rec(i, j + 1)
            down = rec(i + 1, j)
            
            # Calculate the minimum health required to reach the princess
            # while considering the knight's health at each step
            health = min(right, down) - grid[i][j]
            
            # Ensure the knight's health is at least 1
            dp[(i, j)] = max(1, health)
            
            return dp[(i, j)]

        return rec(0, 0)

        