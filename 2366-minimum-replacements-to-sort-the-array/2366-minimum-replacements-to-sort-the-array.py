class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        total_replacements = 0
        current_largest = nums[-1]

        for num in reversed(nums):
            if num <= current_largest:
                current_largest = num
                continue
                
            num_elements = (num + current_largest - 1) // current_largest
            current_largest = num // num_elements
            total_replacements += num_elements - 1

        return total_replacements