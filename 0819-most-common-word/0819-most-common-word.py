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
		#Don't need a counter if you use key function to choose the key with max. count!
        return max(dict, key=dict.get)
        # def remove_special_characters(s):
        #     return re.sub(r'[^\w\s]', '', s)
        # para=para.replace('.','')
        # res=para.replace(",",'')
        # para=remove_special_characters(para)
        # para=list(para.split(" "))
        # para=list(map(str.lower,para))
        # dic={}
        # for i in para:
        #     if i in dic and i not in  ban:
        #         dic[i]+=1
        #     elif i not in ban:
        #         dic[i]=1
        # return max(dic, key= lambda x: dic[x])