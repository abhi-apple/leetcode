class Solution:
    def soupServings(self, n: int) -> float:
        # Define the recursion function with probabilities
        if n >= 4300:
            return 1.0
        def rec(s1, s2, dp):
            if (s1, s2) in dp:
                return dp[(s1, s2)]

            if s1 <= 0 and s2 <= 0:
                return 0.5  # Probability of A and B becoming empty at the same time

            if s1 <= 0:
                return 1.0  # Probability of A becoming empty first

            if s2 <= 0:
                return 0.0  # Probability of B becoming empty first

            prob = 0.25 * (
                rec(s1 - 100, s2, dp) +
                rec(s1 - 75, s2 - 25, dp) +
                rec(s1 - 50, s2 - 50, dp) +
                rec(s1 - 25, s2 - 75, dp)
            )

            dp[(s1, s2)] = prob
            return prob
        dp = {}
        probability_A_empty_first = rec(n, n, dp)

        return probability_A_empty_first 
