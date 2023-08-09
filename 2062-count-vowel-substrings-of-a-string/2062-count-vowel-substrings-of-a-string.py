class Solution:
    def countVowelSubstrings(self, neww: str) -> int:
        vov='aeiou'
        # neww=''
        # for i in word:
        #     if i in vov:
        #         neww=neww+i
        n=len(neww)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                # print(set(neww[i:j+1]))
                if len(set(neww[i:j+1]))==5 and set(neww[i:j+1])==set(vov):
                    cnt+=1
        return cnt
            