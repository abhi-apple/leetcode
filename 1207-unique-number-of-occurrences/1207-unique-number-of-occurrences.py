class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        print(freq)
        ans={}
        for i in freq.values():
            print(i)
            if i in ans:
                return False
            else:
                ans[i]=1
        return True