class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def can(w,dit):
            for i in range(1,len(w)):
                lf=w[:i]
                rt=w[i:]
                if lf in dit:
                    if rt in dit or can(rt,dit):
                        return True
            return False
        res=[]
        dit = set(list(words))
        for w in words:
            if can(w,dit):
                res.append(w)
                
        return res
    