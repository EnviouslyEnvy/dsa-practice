class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # the visited letter coordinates so they may not be visited again in a set or something. when you backtrack pop the coordinate from the set.
        
        result = []
        length = len(word)
        # word=word.split()
        word = list(word)
        rows = len(board)
        cols = len(board[0])
        visited = set()
        curr = []
        def backtrack(j, i, n):
            if n>length:
                return
            # base cases
            if j>=cols or j<0:
                return
            if i>=rows or i<0:
                return
            if (j,i) in visited:
                return
            # visited already case
            visited.add((j,i))
            char = board[i][j]
            curr.append(char)
            if curr == word:
                return True
            elif n==length:
                return
            if char == word[n]:
                if backtrack(j, i-1, n+1):
                    return True
                    # check up
                if backtrack(j+1,i,n+1):
                    return True
                if backtrack(j,i+1,n+1):
                    return True
                if backtrack(j-1,i,n+1):
                    return True
            # base cases, length is over, letter doesn't match word.
            curr.pop()
            visited.remove((j,i))

        for i in range(rows):
            for j in range(cols):
                if backtrack(j,i, 0):
                    return True
        
        return False
    
