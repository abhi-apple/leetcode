from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        fin = []
        
        def rec(i, cur):
            if i == len(s):
                fin.append(cur)
                return
            
            for k in range(i, len(s)):
                if s[i:k+1] == s[i:k+1][::-1]:
                    rec(k + 1, cur + [s[i:k+1]])
        
        rec(0, [])
        return fin
