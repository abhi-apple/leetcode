class Solution:
    def canFinish(self, numCourses: int, prer: List[List[int]]) -> bool:
        maps={i:[] for i in range(numCourses)}
        for crs,pre in prer:
            maps[crs].append(pre)
        vis=set()
        def dfs(crs):
            if crs in vis:
                return False
            if maps[crs]==[]:
                return True
            vis.add(crs)
            for pre in maps[crs]:
                if not dfs(pre):
                    return False
            vis.remove(crs)
            maps[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True