class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr=[]
        row=len(nums)
        for i in range(row):
            col=len(nums[i])
            for j in range(col):
                arr.append([i+j,j,nums[i][j]])
        heapq.heapify(arr)
        # print(arr)
        res=[]
        while arr:
            x,y,val=heapq.heappop(arr)
            # print(ind,val)
            res.append(val)
        return res