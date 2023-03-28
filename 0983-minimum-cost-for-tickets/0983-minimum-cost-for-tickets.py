class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [-1 for _ in range(n+1)]
        
        def da(ind, cost, dp):
            if ind >=n:
                return 0
            if dp[ind] != -1: # if we have computed this day's cost before, return it
                return dp[ind]

            # first we buy a 1-day pass and continue with the rest of the days
            option1 = cost[0] + da(ind+1, cost, dp)

            # then we buy a 7-day pass and continue with the rest of the days
            i = ind
            while i < n and days[i] < days[ind] + 7:
                i += 1
            option2 = cost[1] + da(i, cost, dp)

            # finally we buy a 30-day pass and continue with the rest of the days
            i = ind
            while i < n and days[i] < days[ind] + 30:
                i += 1
            option3 = cost[2] + da(i, cost, dp)

            # store the minimum cost among the three options in the table and return it
            dp[ind] = min(option1, option2, option3)
            return dp[ind]

        return da(0, costs, dp)

