class Solution:
    def ladderLength(self, beg: str, end: str, wrd: List[str]) -> int:
        que=deque([beg])
        cnt=0
        let=len(beg)
        wrd=set(wrd)
        alp='abcdefghijklmnopqrstuvwxyz'
        alp=list(alp)
        while que:
            n=len(que)
            cnt+=1

            for _ in range(n):
                
                var=que.popleft()
                # print(var)
                # print(wrd)
                if var ==end:
                    return cnt
                # if not wrd:
                #     return 0
                var=list(var)
                for k in range(let):
                    test=var[:]
                    
                    
                    for i in alp:
                        test=list(test)
                        
                        test[k]=i
                        test=''.join(test)
                        if test in wrd:
                            
                            que.append(test)
                            wrd.remove(test)
        return 0
        
        
            