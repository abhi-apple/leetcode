class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in edges: 
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        
        size = [0]*n
        
        def fn(a, par): 
            c = s = 0
            for aa in graph.get(a, []): 
                if aa != par: 
                    cc, ss = fn(aa, a)
                    c, s = c + cc, s + ss + cc
            size[a] = c + 1
            return c + 1, s
        
        ans = [0]*n
        ans[0] = fn(0, -1)[1]
        
        stack = [0]
        while stack: 
            x = stack.pop()
            for xx in graph.get(x, []): 
                if not ans[xx]: 
                    ans[xx] = ans[x] + n - 2*size[xx]
                    stack.append(xx)
        return ans 
            
            
            
        