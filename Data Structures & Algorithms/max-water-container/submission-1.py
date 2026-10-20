class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0
        while left < right:
            lh = heights[left]
            rh = heights[right]
            result = max(result, min(lh, rh)*(right-left))
            if lh<rh:
                left +=1
            elif rh<=lh:
                right -=1
            
        return result
        
        