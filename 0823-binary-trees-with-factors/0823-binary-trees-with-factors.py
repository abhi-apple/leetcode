class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dic={}
        for i in arr:
            dic[i]=1
        # main=0
        for i in range(1,len(arr)):
            j=0
            cnt=0
            while j<i:
                if arr[i]%arr[j]==0 and (arr[i]//arr[j]) in dic:
                    # print(dic[arr[i]],dic[arr[j]],i,j)
                    cnt=(cnt+(dic[(arr[i]//arr[j])]*dic[arr[j]]))%(10**9 +7)
                
                j+=1
            dic[arr[i]]+=cnt
            # print(dic)
            # main=(main+cnt)%(10**9 +7)
        return sum(dic.values())%(10**9 +7)
                    
                    
            
        