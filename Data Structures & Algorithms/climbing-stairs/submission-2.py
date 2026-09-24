class Solution:
    def climbStairs(self, n: int) -> int:
        # from collections import defaultdict
        # actually don't need
        memo = {}
        def calc(n):

            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            # memo=defaultdict(int)

            if n not in memo:
                memo[n] = (calc(n-1) + calc(n-2))
            
            return memo[n]
        return calc(n)          