class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        from collections import deque
        
        # heights_indexed=[]
        # for i in range(len(heights)):
            # heights_indexed.append((heights[i],i))
        # # heights_indexed = [(height, i) for i, height in enumerate(heights)].sorted()
        
        # we don't actually need to heights with the index, we can just lookup afterwards.

        stack = []
        max_area=0

        for i,h in enumerate(heights):
            start=i
            # don't know if we can extend back yet
            while stack and stack[-1][1]>h:
                # Check if the last added bar has a higher height (ie current height can stretch back)
                prev_start, prev_height = stack.pop()
                # see the last added index's and height
                max_area=max(max_area, prev_height*(i-prev_start))
                # Since the last added bar is being removed, see if it could create the max area first with the new/current bar in mind.
                start=prev_start
                # Set the new starting point/left stretch point to whatever the last bar's was.
                # As you can see this will propagate as we move forward for as long as it can.
            stack.append((start,h))

        # Look at the heights that remain in the queue - were able to extend to the end. 
        for start, h in stack:
            max_area = max(max_area, h*(len(heights)-start))

        return max_area