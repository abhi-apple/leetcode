class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into a list of words

        if len(pattern) != len(words):  # Check if the number of characters in the pattern and the number of words in the string are equal
            return False

        mapping = [-1] * 26  # Initialize an array of size 26 to store the mapping between characters and words
        for i in range(len(pattern)):
            char = ord(pattern[i]) - ord('a')  # Convert the character to an integer index in the range 0-25
            word = words[i]

            if mapping[char] != -1:  # If the character is already in the mapping, check if it maps to the same word as before
                if mapping[char] != word:
                    return False
            else:  # If the character is not in the mapping, check if the word is already mapped to a different character
                for j in range(26):
                    if mapping[j] == word:
                        return False
                mapping[char] = word  # Add the mapping to the array

        return True  # If all checks pass, return True

#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()  # Split the string into a list of words

#         if len(pattern) != len(words):  # Check if the number of characters in the pattern and the number of words in the string are equal
#             return False

#         mapping = {}  # Initialize an empty dictionary to store the mapping between characters and words
#         for i in range(len(pattern)):
#             char = pattern[i]
#             word = words[i]

#             if char in mapping:  # If the character is already in the mapping, check if it maps to the same word as before
#                 if mapping[char] != word:
#                     return False
#             else:  # If the character is not in the mapping, check if the word is already mapped to a different character
#                 if word in mapping.values():
#                     return False
#                 mapping[char] = word  # Add the mapping to the dictionary

#         return True  # If all checks pass, return True

    # def wordPattern(self, pt: str, s: str) -> bool:
    #     words=s.split()
    #     print(words)
    #     if len(words)!=len(s):
    #         return False
    #     res={}
    #     for i in range(len(pt)):
    #         char=pt[i]
    #         wrd=words[i]
    #         if char in res:
    #             if res[char]!=wrd:
    #                 return False
    #         else:
    #             if wrd in res.values():
    #                 return False
    #             res[char]=wrd
    #     return True