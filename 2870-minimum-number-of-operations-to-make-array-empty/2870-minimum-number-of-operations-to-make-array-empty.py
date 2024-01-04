class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic=Counter(nums)
        cnt=0

        for i in dic:
            if dic[i]==1:
                return -1
            elif dic[i]%3==0:
                cnt+=dic[i]//3
            elif dic[i]%3==2:
                cnt+=(dic[i]//3 +1)
            elif dic[i]%3==1:
                cnt+=(2+(dic[i]-4)//3)
            elif dic[i]%2==0:
                cnt+=dic//2
            else:
                return -1

        return cnt