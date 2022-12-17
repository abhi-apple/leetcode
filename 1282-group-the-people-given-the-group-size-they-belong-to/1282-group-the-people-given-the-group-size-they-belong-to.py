class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp = defaultdict(list)
        op=[]
        for i ,grp in enumerate(groupSizes):
            mp[grp].append(i)
            if len(mp[grp])==grp:
                op.append(mp[grp])
                del mp[grp]
        return op
    

