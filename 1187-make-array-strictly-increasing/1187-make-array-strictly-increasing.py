class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)
        dp = {}

        def rec(i, prev):
            if i == n:
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            ans = float('inf')

            if arr1[i] > prev:
                ans = rec(i + 1, arr1[i])
            id = bisect.bisect_right(arr2, prev)
            if id < len(arr2):
                ans = min(ans, rec(i + 1, arr2[id]) + 1)

            dp[(i, prev)] = ans
            return dp[(i, prev)]

        ret = rec(0, float('-inf'))
        if ret == float('inf'):
            return -1
        return ret
