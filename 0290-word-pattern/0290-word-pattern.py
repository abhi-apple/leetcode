class Solution:
    def wordPattern(self, pt: str, s: str) -> bool:
        words=s.split()
        if len(pt)!=len(words):
            return False
        ctw={}
        wtc={}
        for ch,wo in zip(pt,words):
            if ch in ctw:
                if ctw[ch]!=wo:
                    return False
            elif wo in wtc:
                return False
            else:
                ctw[ch]=wo
                wtc[wo]=ch
        return True