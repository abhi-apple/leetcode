class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp={}
        words.sort(key=len)
        def rec(i,pr):
            def chk(st,com):
                n=len(st)
                m=len(com)
                if m!=n+1:
                    return False
                i=0
                j=0
                chk=False
                while i < n and j < m:
                    if st[i] == com[j]:
                        i += 1
                        j += 1
                        continue
                    if chk:
                        return False
                    j += 1
                    chk = True
                return True
                        
                
            if i==len(words):
                return 0
            if (i,pr) in dp:
                return dp[(i,pr)]
            nt=rec(i+1,pr)
            tk=0
            if pr==-1 or chk(words[pr],words[i]):
                tk=1+rec(i+1,i)
            dp[(i,pr)]=max(tk,nt)
            return dp[(i,pr)]
        return rec(0,-1)