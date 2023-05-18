class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dic={}
        for i in edges:
            if i[1] in dic:
                dic[i[1]].append(i[0])
            else:
                dic[i[1]]=[]
                dic[i[1]].append([i[0]])
        res=[]
        for i in range(n):
            if i not in dic:
                res.append(i)
        return res