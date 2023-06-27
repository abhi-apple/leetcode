class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = stones[-1]
        sets = set(stones)
        if stones[1] != 1:
            return False
        
        @cache
        def rec(i, k):
            if i == n:
                return True
            if i not in sets:
                return False
            for j in [k - 1, k, k + 1]:
                if j > 0 and rec(i + j, j):
                    return True
            return False
        
        return rec(1, 1)
