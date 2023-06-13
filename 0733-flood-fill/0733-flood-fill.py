class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init=img[sr][sc]
        img[sr][sc]=color
        vis=set()
        def dfs(i,j):
            vis.add((i,j))
            dic=[(-1, 0), (0, 1), (1, 0), (0, -1)]
            for d in dic:
                ix,jx=i+d[0],j+d[1]
                if (ix, jx) not in vis and 0 <= ix < len(img) and 0 <= jx < len(img[0]) and img[ix][jx] == init:
                    img[ix][jx]=color
                    dfs(ix,jx)
        dfs(sr,sc)
        return img