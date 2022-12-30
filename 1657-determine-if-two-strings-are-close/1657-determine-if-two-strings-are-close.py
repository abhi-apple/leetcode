class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1)!=len(w2):
            return False
        w1c = [0] * 26
        w2c = [0] * 26
        for c in w1:
            w1c[ord(c) - ord('a')] += 1
        for c in w2:
            w2c[ord(c) - ord('a')] += 1
        if set(w1)!=set(w2):
            return False
        w1c.sort()
        w2c.sort()
        if w1c!=w2c:
            return False
        return True