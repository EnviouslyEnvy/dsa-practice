class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import deque
        
        # So essentially if a fleet's position the next hour is geq to the fleet they merge and maintain the speed of the fleet with the higher starting position as it was ahead.
        # I really really really don't dig this problem.
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        stack=[]
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack)>= 2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)