class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxi=0
        def rec(ind,cur):
            if ind==len(arr):
                return len(cur)
            maxi=len(cur)
            for i in range(ind,len(arr)):
                if len(set(cur+arr[i]))==len(cur+arr[i]):
                    maxi=max(maxi,rec(i+1,cur+arr[i]))
            maxi=max(maxi,rec(ind+1,cur))
            return maxi
                             
        return rec(0,'')