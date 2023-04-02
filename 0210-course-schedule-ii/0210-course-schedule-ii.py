class Solution:
    def findOrder(self, numCourses: int, p: List[List[int]]) -> List[int]:
        maps={i:[] for i in range(numCourses)}
        for crs , pre in p:
            maps[crs].append(pre)
        vis=set()
        cycle=set()
        
        res=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True
            cycle.add(crs)
            for pre in maps[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs)
            vis.add(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return res
            