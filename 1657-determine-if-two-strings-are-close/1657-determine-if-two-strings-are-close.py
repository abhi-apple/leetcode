class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1=list(word1)
        w2=list(word2)
        d1=defaultdict(lambda:0)
        d2=defaultdict(lambda:0)
        for a in w1:
            d1[a]+=1
        for a in w2:
            d2[a]+=1
        d1v=list(d1.values())
        d2v=list(d2.values())
        k1=list(d1.keys())
        k2=list(d2.keys())
        k1.sort()
        k2.sort()
        d1v.sort()
        d2v.sort()
        return d1v==d2v and k1==k2

        # if len(w1)!=len(w2):
        #     return False
        # w1c = [0] * 26
        # w2c = [0] * 26
        # for c in w1:
        #     w1c[ord(c) - ord('a')] += 1
        # for c in w2:
        #     w2c[ord(c) - ord('a')] += 1
        # if set(w1)!=set(w2):
        #     return False
        # w1c.sort()
        # w2c.sort()
        # if w1c!=w2c:
        #     return False
        # return True