class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Initialize the count of strings to 1 for each vowel
        a = e = i = o = u = 1
        
        # Iterate n times to generate all possible strings
        for _ in range(n-1):
            # Update the count of strings for each vowel
            a, e, i, o, u = a+e+i+o+u, e+i+o+u, i+o+u, o+u, u
        
        # Return the total count of strings
        return a+e+i+o+u
