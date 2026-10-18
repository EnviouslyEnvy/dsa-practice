class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # at all times open>=close

        result = []
        curr=[]
        max_parenthesis = n*2
        def backtrack(open_count, close_count):
            if open_count<close_count:
                return
            
            if open_count == n and close_count == n:
                result.append(''.join(curr))
                return
            
            if open_count+1<=n:
                curr.append('(')
                backtrack(open_count+1, close_count)
                curr.pop()
            if close_count+1<=n:
                curr.append(')')
                backtrack(open_count, close_count+1)
                curr.pop()
        backtrack(0, 0)
        return result