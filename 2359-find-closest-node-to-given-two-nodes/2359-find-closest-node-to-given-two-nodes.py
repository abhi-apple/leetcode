class Solution:
    def closestMeetingNode(self, edges: List[int], nd1: int, nd2: int) -> int:
        def store(i,dis,edges,pat):
            if i!=-1 and pat[i]==-1:
                pat[i]=dis
                
                store(edges[i],dis+1,edges,pat)
            
        ans=-1
        mind=100000
        n=len(edges)
        pat1=[-1]*n
        pat2=[-1]*n
        store(nd1,0,edges,pat1)
        store(nd2,0,edges,pat2)
        for i in range(n):
            
            if min(pat1[i],pat2[i])>=0 and max(pat1[i],pat2[i])<mind:
              
                mind=max(pat1[i],pat2[i])
                ans=i
        return ans