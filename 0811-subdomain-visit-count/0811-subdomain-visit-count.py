class Solution:
    def subdomainVisits(self, abc: List[str]) -> List[str]:
        couns=defaultdict(int)
        for cd in abc:
            coun,dom=cd.split(' ')
            coun=int(coun)
            sub=dom.split('.')
            for i in range(len(sub)-1,-1,-1):
                couns['.'.join(sub[i:])]+=coun
        return [' '.join([str(count),dom]) for dom,count in couns.items()]