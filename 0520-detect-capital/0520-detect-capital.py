class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        for i in range(1,len(word)):
            print(ord(word[i]))
            if ord(word[0])>=97 and ord(word[i])<97:
                print("h1")
                return False 
            else:
                if ord(word[1])<97 and ord(word[i])>=97:
                    print("h2")
                    return False 
                elif ord(word[i])<97 and ord(word[1])>=97:
                    print("h3")
                    return False 
        return True