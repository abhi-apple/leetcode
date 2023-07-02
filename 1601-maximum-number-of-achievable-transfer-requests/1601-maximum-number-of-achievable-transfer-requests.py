class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transferList = [0] * n
        maxRequests = 0
        def dfs(i, transferCount):
            nonlocal maxRequests
            if i == len(requests):
                for transfer in transferList:
                    if transfer != 0:
                        return

                maxRequests = max(maxRequests, transferCount)
                return

            # Either perform the current transfer
            transferList[requests[i][0]] -= 1
            transferList[requests[i][1]] += 1
            dfs(i + 1, transferCount + 1)
            # Or skip the current transfer after reverting the changes made in the current state
            transferList[requests[i][0]] += 1
            transferList[requests[i][1]] -= 1
            dfs(i + 1, transferCount)

        dfs(0, 0)
        return maxRequests