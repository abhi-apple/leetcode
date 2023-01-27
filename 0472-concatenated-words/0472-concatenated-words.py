class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def can(w,dit):
            if w in dp:
                return True
            for i in range(mini,len(w)):
                lf=w[:i]
                rt=w[i:]
                if lf in dit:
                    if rt in dit or can(rt,dit):
                        dp.append(w)
                        return True
            return False
        res=[]
        dit = set(list(words))
        mini=10000
        dp=[]
        for w in words:
            mini=min(len(w),mini)
        for w in words:
            if can(w,dit):
                res.append(w)
                
        return res
    