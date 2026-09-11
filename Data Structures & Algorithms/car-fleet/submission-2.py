class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import deque
        
        # So essentially if a fleet's position the next hour is geq to the fleet they merge and maintain the speed of the fleet with the higher starting position as it was ahead.
        # I really really really don't dig this problem.
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        # Order the cars in reverse order by position (descending), such that the closest cars to the target are first in the list.
        stack=[]
        for p,s in pair:
            stack.append((target-p)/s)
            # Add times to reach the end.
            if len(stack)>= 2 and stack[-1]<=stack[-2]:
                # If the very last car has a lower time to reach than the car ahead, it merges.
                stack.pop()
        return len(stack)