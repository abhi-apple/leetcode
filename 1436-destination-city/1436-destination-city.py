class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic=[]
        for i in paths:
            dic.append(i[0])
        for i in paths:
            if i[1] not in dic:
                return i[1]
        return 1
    