class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f1="qwertyuiop"
        f2="asdfghjkl"
        f3="zxcvbnm"
        ans=[]
        sm=words.copy()
        sm=[x.lower() for x in sm]
        print(words)
        def k1(k):
            print("h1")
            for i in k:
                print(i)
                if i not in f1:
                    return False
            return True
        def k2(k):
            print("h2")
            for i in k:
                print(i)
                if i not in f2:
                    return False
            return True
        def k3(k):
            print("h3")
            for i in k:
                print(i)
                if i not in f3:
                    return False
            return True
        for i in range(len(sm)):
            if k1(sm[i]) or k2(sm[i]) or k3(sm[i]):
                print("h123")
                ans.append(words[i])

                
                
        return ans