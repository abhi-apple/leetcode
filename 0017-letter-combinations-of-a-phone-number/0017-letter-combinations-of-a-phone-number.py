class Solution:
    def letterCombinations(self, dig: str) -> List[str]:
        kv = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n=len(dig)
        fin=[]
        if not dig:
            return []
        def rec(i,pat):
            if i==n:
                fin.append(pat)
                return 
            if dig[i] in kv:
                for k in kv[dig[i]]:
                    rec(i+1,pat+k)
            return
                    
                
        dig=list(dig)
        rec(0,'')
        return fin
    
    