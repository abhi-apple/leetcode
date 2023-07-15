class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        stack=deque()
        word=list(beginWord)
        stack.append(word)
        alp='abcdefghijklmnopqrstuvwxyz'
        wordList=set(wordList)
        if len(beginWord)!=len(endWord) or endWord not in wordList:
            return 0
        cnt=0
        while stack:
            n=len(stack)
            for _ in range(n):
                wrd=stack.popleft()
                if ''.join(wrd)==endWord:
                    return cnt+1
                for i in range(len(wrd)):
                    tmp=wrd[i]
                    for k in alp:
                        
                        wrd[i]=k
                        new_word = ''.join(wrd)
                        if new_word in wordList:
                            stack.append(list(wrd))
                            wordList.remove(new_word)
                    wrd[i]=tmp
            cnt+=1
        return 0

    
    
# from collections import deque

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         stack = deque()
#         stack.append(list(beginWord))
#         alp = 'abcdefghijklmnopqrstuvwxyz'
#         wordList = set(wordList)
#         if len(beginWord) != len(endWord) or endWord not in wordList:
#             return 0
#         cnt = 0
#         while stack:
#             n = len(stack)
#             for _ in range(n):
#                 wrd = stack.popleft()
#                 if ''.join(wrd) == endWord:
#                     return cnt + 1
#                 for i in range(len(wrd)):
#                     tmp = wrd[i]
#                     for k in alp:
#                         wrd[i] = k
#                         new_word = ''.join(wrd)
#                         if new_word in wordList:
#                             stack.append(list(wrd))  # Add a copy of the word
#                             wordList.remove(new_word)  # Remove the word from wordList
#                     wrd[i] = tmp
#             cnt += 1
#         return 0

                    
                
            