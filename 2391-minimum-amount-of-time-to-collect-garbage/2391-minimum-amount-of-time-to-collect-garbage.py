class Solution:
    def garbageCollection(self, gar: List[str], tra: List[int]) -> int:
        dic={}
        for var in range(len(gar)):
            res=list(gar[var])
            for i in res:
                dic[i]=var
            
        tot=0
        for i in range(len(gar)):
            if 'P' in list(gar[i]):
                tot+=gar[i].count('P')
        for i in range(len(gar)):
            if 'G' in list(gar[i]):
                tot+=gar[i].count('G')
        for i in range(len(gar)):
            if 'M' in list(gar[i]):
    
                tot+=gar[i].count('M')
        for i in dic:
            if dic[i]!=0:
                tot+=sum(tra[:dic[i]])
            
        return tot
        