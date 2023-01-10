class Solution:
    def findLongestWord(self, s: str, dic: List[str]) -> str:
        dic.sort(key = lambda x: (-len(x),x))
        for word in dic:
            j = 0 
            for i in range(len(s)):
                if s[i] == word[j]: j+=1

                if j == len(word): return word

        return ''
