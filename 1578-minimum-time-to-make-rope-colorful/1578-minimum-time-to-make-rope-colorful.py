class Solution:
    def minCost(self, colors: str, cost: List[int]) -> int:
        n = len(colors)
        prev = cost[0]
        res = 0
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                res += min(cost[i], prev)
                prev = max(cost[i], prev)
            else:
                prev = cost[i]
        return res