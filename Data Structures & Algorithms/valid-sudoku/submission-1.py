class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares = collections.defaultdict(set)
        # Square key is (r-1)//3, (c-1)//3
        # actually don't need to minus 1 since python range starts from 0.
        for r in range(9):
            for c in range(9):
                current=board[r][c]
                if current=='.':
                    continue
                if current not in rows[r]:
                    rows[r].add(current)
                else:
                    return False
                if current not in cols[c]:
                    cols[c].add(current)
                else:
                    return False
                row_group=r//3
                col_group=c//3
                # we will set the keys for each group's set using these
                if current not in squares[(row_group, col_group)]:
                    squares[(row_group,col_group)].add(current)
                else:
                    return False
        return True