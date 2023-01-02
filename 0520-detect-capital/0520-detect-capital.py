class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all characters are capital letters
        if word.isupper():
            return True
        # Check if all characters are not capital letters
        elif word.islower():
            return True
        # Check if only the first character is a capital letter
        elif len(word) > 1 and word[0].isupper() and word[1:].islower():
            return True
        # Otherwise, capital usage is not correct
        else:
            return False
