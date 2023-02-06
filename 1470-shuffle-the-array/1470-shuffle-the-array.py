class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        fir=nums[:n]
        ls=nums[n:]
        fin=[]
        for i in range(n):
            fin.append(fir[i])
            fin.append(ls[i])
        return fin