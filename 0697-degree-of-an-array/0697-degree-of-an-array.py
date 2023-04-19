class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i
            else:
                dic[nums[i]] = [1, i, i]
                
        max_degree = max([v[0] for v in dic.values()])
        shortest_subarray_len = float('inf')
        for v in dic.values():
            if v[0] == max_degree:
                shortest_subarray_len = min(shortest_subarray_len, v[2] - v[1] + 1)
                
        return shortest_subarray_len
