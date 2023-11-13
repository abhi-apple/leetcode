class Solution:
    def sortVowels(self, s: str) -> str:
        dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

        for i in s:
            if i in dic:
                dic[i]+=1
        ans=''
        for i in s:
            if i in dic:
                # bol=False
                for k in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                    if dic[k]>0 :
                        dic[k]-=1
                        ans+=k
                        break
                        # bol=True
            else:
                ans+=i
        return ans