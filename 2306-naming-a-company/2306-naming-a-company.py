class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        names=defaultdict(set)
        res=0  
        for i in ideas:
            names[i[0]].add(i[1:])
        arr=list(names.keys())
        ans,n=0,len(arr)
        
        for i in range(n):
            for j in range(i+1,n):
                a,b=arr[i],arr[j]
                res+=len(names[a]-names[b])*len(names[b]-names[a])*2
                
        return res