class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp = {}

        def rec(i, bol, cnt):
            if cnt == 0:
                return 0
            if i == len(p):
                return 0
            if (i, bol, cnt) not in dp:
                # Added the `not in` check here
                if bol:
                    dp[(i, bol, cnt)] = max(-p[i] + rec(i + 1, not bol, cnt ), rec(i + 1, bol, cnt))
                else:
                    dp[(i, bol, cnt)] = max(p[i] + rec(i + 1, not bol, cnt-1), rec(i + 1, bol, cnt))
            return dp[(i, bol, cnt)]

        return rec(0, True, 2)
