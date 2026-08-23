class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_water=0
        distance=len(heights)-1
        while left<right:
            vol=min(heights[left],heights[right])*distance
            if vol>max_water:
                max_water=vol
            if heights[left]<heights[right]:
                left+=1
                distance-=1
            else:
                right-=1
                distance-=1
        return max_water