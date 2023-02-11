class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        
        # build graph
        adjList = {i:[] for i in range(n)} # {0: [(1, 'r'), 1:[], 2:[1, 'b']}
        for start, end in red_edges:
            adjList[start].append((end, 'r'))
        for start, end in blue_edges:
            adjList[start].append((end, 'b'))
        
        ans = [-1] * n
        ans[0] = 0
        
        # do bfs by increasing level every time
        stack = []
        for nextPtr, color in adjList[0]:
            stack.append((nextPtr, color)) # (position, color)
        
        visited = {(0, 'r'), (0, 'b')} 
        level = 0
        while stack:
            level += 1
            nextStack = []
            for node, color in stack:
                if ans[node] == -1:
                    ans[node] = level
                else:
                    ans[node] = min(ans[node], level)
                for nextPtr, nextColor in adjList[node]:
                    if color != nextColor and (nextPtr, nextColor) not in visited:
                        nextStack.append((nextPtr, nextColor))
                        visited.add((nextPtr, nextColor))
            
            stack = nextStack
        
        return ans