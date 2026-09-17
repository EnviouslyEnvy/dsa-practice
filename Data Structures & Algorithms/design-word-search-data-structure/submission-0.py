# Use a trie
# Explore all branches recursively when encountering a '.'
# Since using a dictionary implementation of trie, we just need to iterate through all values (which are just other nodes).
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur=self.root

        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            # Set the current 'node' to the child node that's next or that you just added
            cur = cur.children[c]
        # after going through all the characters mark that node as the end of a word.
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # We don't want to use this function bare, as we want to recursively call a function per-character.
        # If we do it using the normal trie method, then we end up traversing all letters before the period character for each character substitute we try.
        # At least in my first implementation idea
        # cur=self.root
    
        # for c in word:
        #     if c=='.':
        #         for next_letter in cur.children.keys()
        #             self.search()


        def dfs(i, cur):
            if i == len(word):
                return cur.endOfWord
            
            c = word[i]

            if c == '.':
                for child in cur.children.values():
                    if dfs(i+1, child):
                        # If we can find the next character among the children's next node mappings...
                        return True
                return False
            
            if c not in cur.children:
                return False
            
            return dfs(i + 1, cur.children[c])
        
        return dfs(0, self.root)
