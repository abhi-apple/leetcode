class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = [0]*n
        def dfs(node, parent):
            count = [0]*26
            for child in graph[node]:
                if child != parent:
                    child_count = dfs(child, node)
                    for i in range(26):
                        count[i] += child_count[i]
            count[ord(labels[node]) - ord('a')] += 1
            ans[node] = count[ord(labels[node]) - ord('a')]
            return count

        dfs(0, -1)
        return ans