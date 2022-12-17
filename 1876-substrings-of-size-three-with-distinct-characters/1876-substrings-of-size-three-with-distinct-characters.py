class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        # Iterate through the string, looking at substrings of length 3
        for i in range(len(s) - 2):
            # Check if the substring has no repeated characters
            if len(set(s[i:i+3])) == 3:
                count += 1

        return count