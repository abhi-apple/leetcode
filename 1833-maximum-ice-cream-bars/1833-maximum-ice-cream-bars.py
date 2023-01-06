class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins<costs[0]:
            return 0
        sums=0
        cnt=0
        for i in costs:
            sums+=i
            cnt+=1
            if sums>coins:
                cnt-=1
                break
        return cnt
                