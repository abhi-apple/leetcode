from heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, hei: List[List[int]]) -> int:
        dic=[[float('inf') for i in range(len(hei[0]))] for j in range(len(hei))]
        que=[]
        heappush(que,(0,0,0))
        dic[0][0]=0
        while que:
            dis,i,j=heappop(que)
            if i==len(hei)-1 and j==len(hei[0])-1:
                return dis
            dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for d in dire:
                ix,jx=i+d[0],j+d[1]
                if 0<=ix<len(hei) and 0<=jx<len(hei[0]) and dic[ix][jx]>max(dis,abs(hei[i][j]-hei[ix][jx])):
                    dic[ix][jx]=max(dis,abs(hei[i][j]-hei[ix][jx]))
                    heappush(que,(dic[ix][jx],ix,jx))
        
                