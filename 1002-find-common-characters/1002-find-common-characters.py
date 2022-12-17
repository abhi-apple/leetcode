class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        com=list(words[0])
        print(com)
        if len(words)==1:
            return list(words)
        for i in words:
            for j in list(com):
                if j not in i:
                    com.remove(j)
                    print(j,i,"if")
                else:
                    i=i.replace(j, '', 1)
                    print(j,i,"else")
                    # i.replace(j, '')
                    
        return com