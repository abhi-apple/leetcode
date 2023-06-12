class Solution:
    def combinationSum2(self, cd: List[int], tar: int) -> List[List[int]]:
        cd.sort()
        fin=[]
        def rec(i,arr,sums):
            if sums==0:
                arr.sort()
                if arr not in fin:
                    
                    fin.append(arr)
                    return 
            if i==len(cd):
                return 
            for k in range(i,len(cd)):
                if k>i and cd[i]==cd[i-1]:
                    continue
                if sums-cd[k]<0:
                    break
                rec(k+1,arr+[cd[k]],sums-cd[k])
        rec(0,[],tar)
        return fin