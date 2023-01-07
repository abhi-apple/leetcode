class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        sums=0
        st=0
        for i in range(len(gas)):
            sums+=gas[i]-cost[i]
            if sums<0:
                st=i+1
                sums=0

        return st