class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        eve = []
        odd = []
        evet = []
        oddt = []
        for i in nums:
            if i & 1 == 1:
                odd.append(i)
            else:
                eve.append(i)
        for i in target:
            if i & 1 == 1:
                oddt.append(i)
            else:
                evet.append(i)

        eve.sort()
        odd.sort()
        evet.sort()
        oddt.sort()

        # Compare elements at the same index in the sorted lists and calculate the difference
        cnt = 0
        for i in range(len(eve)):
            cnt += abs(evet[i] - eve[i]) // 2

        for i in range(len(odd)):
            cnt += abs(oddt[i] - odd[i]) // 2

        return cnt // 2
