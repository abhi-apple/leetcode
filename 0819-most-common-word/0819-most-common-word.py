import re
class Solution:
    def mostCommonWord(self, para: str, ban: List[str]) -> str:
        dict = {}
        ban = set(ban)
        for c in "!?',;.":
            para = para.replace(c, " ")
        para = para.lower().split()
        for word in para:            
            if word not in ban:
                if word in dict:
                    dict[word]+=1
                else:
                    dict[word]=1
        return max(dict, key=dict.get)
