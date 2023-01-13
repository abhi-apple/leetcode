class Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        n = len(parents)
        for i in range(1, n):
            if s[i] == s[parents[i]]:
                parents[i] = -1
        
        children = [[] for _ in range(n)]
        for i, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(i)

        self.res = 0

        def dfs(i):
            max1 = max2 = 0
            for child in children[i]:
                length = dfs(child)
                if length >= max1:
                    max1, max2 = length, max1
                elif length > max2:
                    max2 = length
            self.res = max(self.res, 1 + max1 + max2)
            return 1 + max1
        
        for i, parent in enumerate(parents):
            if parent == -1:
                dfs(i)
        return self.res