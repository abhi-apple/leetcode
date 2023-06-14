class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        dic = {}
        for i in range(len(graph)):
            dic[i] = []
            for k in graph[i]:
                dic[i].append(k)
            if dic[i] == []:
                ans.append(i)
        
        def dfs(node, st, vis, memo):
            if node in vis:
                return False
            if node in memo:
                return memo[node]

            vis.add(node)
            for var in dic[node]:
                if not dfs(var, st, vis, memo):
                    memo[node] = False
                    return False

            vis.remove(node)
            memo[node] = True
            return True

        vis = set()
        memo = {}
        for i in dic:
            if dic[i] != []:
                st = i
                if i not in vis and dfs(i, st, vis, memo):
                    ans.append(i)

        return sorted(ans)

                
