class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        fin = set()
        n = len(arr)
        dp = {}

        def rec(i, ors):
            if (i, ors) in dp:
                return dp[(i, ors)]

            if ors not in fin:
                fin.add(ors)

            if i == n:
                return

            rec(i + 1, ors | arr[i])
            dp[(i, ors)] = None  # Store the result to avoid recomputation
            return

        for i in range(n):
            rec(i, arr[i])

        return len(fin)

            