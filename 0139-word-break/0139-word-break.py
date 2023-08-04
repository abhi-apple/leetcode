class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}
        
        def rec(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for k in range(i, len(s)):
                if s[i:k+1] in wordSet and rec(k+1):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return rec(0)
