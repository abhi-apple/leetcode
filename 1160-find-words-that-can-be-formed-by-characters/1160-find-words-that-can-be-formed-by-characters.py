class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars=list(chars)
        maind=Counter(chars)
        ans=0
        for word in words:
            form=True
            for j in set(word):
                if maind[j]<word.count(j):
                    form=False
                    break
            if form:
                ans+=len(word)
        return ans
                
                
                
            
        