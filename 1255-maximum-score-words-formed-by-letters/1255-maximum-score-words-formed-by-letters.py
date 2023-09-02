# class Solution:
#     def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
#         dic={}
#         for i in set(letters):
#             dic[i]=letters.count(i)
#         n=len(words)
#         dp={}
#         def rec(i,dic):
#             if i==n:
#                 return 0
#             if i in dp:
#                 return dp[i]
#             dp[i]=0
#             ntk=rec(i+1,dic)
#             dp[i]=max(dp[i],ntk)
#             tk=0
#             sc=0
#             for k in words[i]:
#                 if k not in dic or dic[k]==0:
#                     return dp[i]
#                 else:
#                     sc+=score[ord(k)-ord('a')]
#                     dic[k]-=1
#             tk=rec(i+1,dic)+sc
#             for k in words[i]:
#                 dic[k]+=1
#             dp[i]=max(tk,ntk)
#             return dp[i]
            
            
#         return rec(0,dic)


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def count_letters(word):
            letter_count = [0] * 26
            for letter in word:
                letter_count[ord(letter) - ord('a')] += 1
            return letter_count

        def can_form_word(word, available_letters):
            word_count = count_letters(word)
            for i in range(26):
                if word_count[i] > available_letters[i]:
                    return False
            return True

        def calculate_score(word):
            word_score = 0
            for letter in word:
                word_score += score[ord(letter) - ord('a')]
            return word_score

        def dfs(index, available_letters):
            if index == len(words):
                return 0

            # Skip the current word
            max_score = dfs(index + 1, available_letters)

            # Try to use the current word if possible
            if can_form_word(words[index], available_letters):
                word_score = calculate_score(words[index])
                new_letters = list(available_letters)
                for letter in words[index]:
                    new_letters[ord(letter) - ord('a')] -= 1
                max_score = max(max_score, word_score + dfs(index + 1, new_letters))

            return max_score

        available_letters = count_letters(letters)
        return dfs(0, available_letters)
