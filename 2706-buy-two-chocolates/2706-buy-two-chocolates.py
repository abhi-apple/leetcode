class Solution:
    def buyChoco(self, pr: List[int], money: int) -> int:
        pr.sort()
        res=[]
        for i in range(len(pr)):
            for j in range(i+1,len(pr)):
                res.append(pr[i]+pr[j])
        res.sort(reverse=True)
        while res and res[-1]>money:
            res.pop()
        if not res:
            return money
        return money-res[-1]
    