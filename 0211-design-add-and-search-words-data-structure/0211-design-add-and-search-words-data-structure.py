class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie['word'] = word
        
    def search(self, word):
        return self.helper(self.trie, word)
    
    def helper(self, trie, word):
        if not word:
            return True if trie.get('word') else False

        if word[0] == '.':
            for c in trie:
                if c != 'word' and self.helper(trie[c], word[1:]):
                    return True
        elif word[0] in trie:
            return self.helper(trie[word[0]], word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)