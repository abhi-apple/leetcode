class Solution:
    def findWinners(self, mat: List[List[int]]) -> List[List[int]]:
        dic={}
        for w,l in mat:
            if w not in dic:
                dic[w]=''
            if l in dic:
                dic[l]+='l'
            else:
                dic[l]='l'
        ans=[[],[]]
        for i in sorted(dic):
            if dic[i]=='':
                ans[0].append(i)
            elif dic[i]=='l':
                ans[1].append(i)
        return ans
            
                