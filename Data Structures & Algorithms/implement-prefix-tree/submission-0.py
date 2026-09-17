class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        # End of word will indicate that at that character the node ends 
        
        # insert will be like children["a"] = TrieNode()

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c] # shift pointer to appropriate child node.
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True