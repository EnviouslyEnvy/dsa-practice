class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
    def addWord(self, word):
        cur = self
        # get current pointer to be at root node (the self node)
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                # If character node does not exist from current add it
            
            cur = cur.children[c]
            # navigate to that character node
        cur.isWord = True
        

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Make the trie 
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        num_rows, num_cols = len(board)-1, len(board[0])-1
        visited = set()
        result = set()

        def dfs(r, c, node, word):
            if (r<0 or r>num_rows or c<0 or c>num_cols or (r, c) in visited or board[r][c] not in node.children):
                # That last one ensuring that the character is not in the valid word path trie.
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                result.add(word)
            
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))
        
        for r in range(num_rows+1):
            for c in range(num_cols+1):
                dfs(r, c, root, '')

        return list(result)