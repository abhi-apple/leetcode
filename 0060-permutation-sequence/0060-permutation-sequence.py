class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        nums = list(range(1, n+1))
        factorial = [1] * (n + 1)
        for i in range(1, n+1):
            factorial[i] = factorial[i-1] * i
        k -= 1
        for i in range(n, 0, -1):
            first_num_index = k // factorial[i-1]
            res.append(nums[first_num_index])
            nums.pop(first_num_index)
            k -= first_num_index * factorial[i-1]
        return "".join(map(str, res))

        